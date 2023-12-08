from django.urls import path

from .views import (
    LoginView,
    SignUpView,
    ResetPasswordView,
    LogoutView,
)


urlpatterns = [
    path("login/", LoginView.as_view()),
    path("signup/", SignUpView.as_view()),
    path("reset_password/", ResetPasswordView.as_view()),
    path("logout/", LogoutView.as_view()),
]
