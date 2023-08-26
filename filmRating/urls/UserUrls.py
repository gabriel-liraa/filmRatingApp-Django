from django.urls import path
from filmRating.views.UserViews import login_view, logout_view, register_user_view

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_user_view, name="register"),
]
