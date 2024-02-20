from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from.models import Post, Category, Comment, Profile #modelde oluşturulanı import etmek önemli
from .forms import PostForm, EditForm, CommentForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# def home(request):
# return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post 
    template_name = "home.html"
    ordering = ["-post_date"]

def CategoryListView(request):
    cat_menu_list = Category.objects.all().order_by('name')
    return render(request, "category_list.html", {"cat_menu_list": cat_menu_list})

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace("-"," ").lower()).order_by("-post_date")
    if(category_posts.count() != 0):
        return render(request, "categories.html", {"cats": cats.replace("-"," ").title(), "category_posts": category_posts, "empty": False})
    else:
        return render(request, "categories.html", {"cats": cats.replace("-"," ").title(), "category_posts": category_posts, "empty": True})

class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = post.total_likes()

        if self.request.user.is_authenticated:
            if Profile.objects.filter(user=self.request.user):
                profile = Profile.objects.get(user=self.request.user)
                subscribed = False
                if profile.subscriptions.filter(id=post.author.id).exists():
                    subscribed = True
                context["subscribed"] = subscribed
        
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context
    
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(ArticleDetailView, self).dispatch(*args, **kwargs)

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    success_url = reverse_lazy("home")
    
    def get_context_data(self, *args, **kwargs):
        context = super(AddPostView, self).get_context_data(*args, **kwargs)
        if self.request.user.id != None:
            if Profile.objects.filter(user = self.request.user).exists():
                context["profile"] = Profile.objects.get(user = self.request.user)
                return context
        context["profile"] = None
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)
    
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(AddPostView, self).dispatch(*args, **kwargs)

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "add_comment.html"
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(AddCommentView, self).get_context_data(*args, **kwargs)
        if self.request.user.id != None:
            if Profile.objects.filter(user = self.request.user).exists():
                context["profile"] = Profile.objects.get(user = self.request.user)
                return context
        context["profile"] = None
        return context

    def get_success_url(self):
        return reverse("article_detail", args=[str(self.kwargs['pk'])])
    
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(AddCommentView, self).dispatch(*args, **kwargs)

class AddCategoryView(CreateView):
    model = Category
    template_name = "add_category.html"
    fields = ["name"]
    
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(AddCategoryView, self).dispatch(*args, **kwargs)

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "update_post.html"
    
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(UpdatePostView, self).dispatch(*args, **kwargs)

class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")
    
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(DeletePostView, self).dispatch(*args, **kwargs)

# def LikeView(request, pk):
#     post = get_object_or_404(Post, id=request.POST.get("post_id"))
#     liked = False
#     if post.likes.filter(id=request.user.id).exists():
#         post.likes.remove(request.user)
#     else:
#         post.likes.add(request.user)      
#         liked = True         
#     return HttpResponseRedirect(reverse("article_detail", args=[str(pk)]))

def LikeView(request):
    if request.method == "POST":
        post_id = request.POST.get("post_id")
        user = request.user
        post = get_object_or_404(Post, id=post_id)
        if post.likes.filter(id=user.id).exists():
            post.likes.remove(user)
            return JsonResponse({"status":"unliked"} )
        else:
            post.likes.add(user)
            return JsonResponse({"status":"liked"})
        return JsonResponse({"status":"error" })

@csrf_exempt
def SearchPosts(request):
    if request.method == "POST":
        searched = request.POST['post_searched'] #Çalışmazsa () koy 
        if searched != "":
            posts = Post.objects.filter(body__contains = searched)
            return render(request, 'searched_posts.html', {"searched": searched, "posts": posts})
        else:
           return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")

class SubscribtionListView(ListView):
    model = Post
    template_name = "subscribed_posts.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SubscribtionListView, self).get_context_data(*args, **kwargs)
        profile = get_object_or_404(Profile, id=self.kwargs['pk'])
        subscribed_users = profile.subscriptions.all()
        subscribed_posts = Post.objects.filter(author__in = subscribed_users).order_by("-post_date")
        context["posts"] = subscribed_posts
        return context

    def get_success_url(self):
        current_user = self.request.user
        if current_user.id == self.kwargs['pk']:
            return reverse("subscription", args=[str(self.kwargs['pk'])])
        else:
            return HttpResponseRedirect("/")
