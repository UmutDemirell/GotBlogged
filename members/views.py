from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy, reverse
from .forms import EditProfileForm, PasswordChangingForm, ProfilePageForm
from django.contrib.auth.views import PasswordChangeView
from theblog.models import Profile, Post
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = "registration/create_user_profile_page.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
    
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(CreateProfilePageView, self).dispatch(*args, **kwargs)

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = "registration/edit_profile_page.html"
    form_class = ProfilePageForm  

    def get_success_url(self):
          profileid=self.kwargs['pk']
          return reverse_lazy('profile_page', kwargs={'pk': profileid})
    
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(EditProfilePageView, self).dispatch(*args, **kwargs)

class ProfilePageView(DetailView):
    model = Profile
    template_name = "registration/user_profile.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs["pk"])
        posted = Post.objects.filter(author=page_user.user)

        if self.request.user.is_authenticated:
            if Profile.objects.filter(user=self.request.user):
                profile = Profile.objects.get(user=self.request.user)
                subscribed = False
                if profile.subscriptions.filter(id=page_user.user.id).exists():
                    subscribed = True
                context["subscribed"] = subscribed
            
        context["page_user"] = page_user
        context["posted"] = posted
        return context
    
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(ProfilePageView, self).dispatch(*args, **kwargs)
    
class UserRegisterView(generic.CreateView):
    model = User
    fields = ["username", "first_name", "last_name", "email", "password"]
    template_name = "registration/register.html"
   
    def form_valid(self, form):
        form.instance.set_password(form.cleaned_data['password'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("login")
    
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(UserRegisterView, self).dispatch(*args, **kwargs)

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, *args, **kwargs):
        context = super(UserEditView, self).get_context_data(*args, **kwargs)
        if self.request.user.id != None:
            if Profile.objects.filter(user = self.request.user).exists():
                context["profile"] = Profile.objects.get(user = self.request.user)
                return context
        context["profile"] = None
        return context

    def get_object(self):
        return self.request.user
    
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(UserEditView, self).dispatch(*args, **kwargs)
    
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = "registration/change_password.html"
    success_url = reverse_lazy("password_success")
    
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(PasswordsChangeView, self).dispatch(*args, **kwargs)

def PasswordSuccessView(request):
    return render(request, "registration/password_success.html", {})

def SubscribeView(request,pk):
    subscribed_user = get_object_or_404(User, id=pk)
    
    if Profile.objects.filter(user=request.user):
        if request.user.profile.subscriptions.filter(id = subscribed_user.id).exists():
            request.user.profile.subscriptions.remove(subscribed_user)
        else:
            request.user.profile.subscriptions.add(subscribed_user)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

