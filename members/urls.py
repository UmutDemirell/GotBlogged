from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserRegisterView, UserEditView, PasswordsChangeView, PasswordSuccessView, ProfilePageView, EditProfilePageView, CreateProfilePageView, SubscribeView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", csrf_exempt(auth_views.LoginView.as_view(template_name = "registration/login.html")), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("edit-profile/", UserEditView.as_view(), name="edit_profile"),
    path("password/", PasswordsChangeView.as_view(), name="change_password"),
    path("password-success", PasswordSuccessView, name="password_success"),
    path("<int:pk>/profile/", ProfilePageView.as_view(), name="profile_page"),
    path("<int:pk>/edit-profile-page/", EditProfilePageView.as_view(), name="edit_profile_page"),
    path("create-profile-page/", CreateProfilePageView.as_view(), name="create_profile_page"),
    path("subscribe/<int:pk>", SubscribeView, name="subscribe_to_user"),
    path('reset-password/', csrf_exempt(auth_views.PasswordResetView.as_view(template_name = "registration/reset_password.html")), name="reset_password"),
    path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(template_name = "registration/reset_password_complete.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', csrf_exempt(auth_views.PasswordResetConfirmView.as_view(template_name = "registration/reset_password_form.html")), name="password_reset_confirm"),
    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "registration/reset_password_success.html"), name="password_reset_complete"),
]
