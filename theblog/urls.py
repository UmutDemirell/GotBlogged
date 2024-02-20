from django.urls import path
#from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView, AddCommentView, SearchPosts, SubscribtionListView #kendi verdiğimiz views import etmek önemli
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    #path("", views.home, name="home"),
    path("", HomeView.as_view(), name="home"),
    path("article/<int:pk>", ArticleDetailView.as_view(), name ="article_detail"), #pk = primary key
    path("add-post/", AddPostView.as_view(), name = "add_post"),
    path("add-category/", csrf_exempt(AddCategoryView.as_view()), name = "add_category"),
    path("article/edit/<int:pk>", UpdatePostView.as_view(), name = "update_post"),
    path("article/<int:pk>/remove", DeletePostView.as_view(), name = "delete_post"),
    path("category/<str:cats>", CategoryView, name = "category"),
    path("category-list", CategoryListView, name = "category_list"),
    path("like", LikeView, name="like_post"),
    path("article/<int:pk>/comment", AddCommentView.as_view(), name="add_comment"),
    path("search_posts", SearchPosts , name = "search_posts"),
    path("subscribed/<int:pk>", SubscribtionListView.as_view(), name="subscription"),
]
