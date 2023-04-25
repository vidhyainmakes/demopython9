from django.urls import path
from . import views

from .views import UserRegistrationView, LogoutView, UserLoginView

app_name = 'accounts'

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="user_login"),
    path("logout/", LogoutView.as_view(), name="user_logout"),
    path("register/", UserRegistrationView.as_view(), name="user_registration"),
    path("", views.allbranch, name="allbranch"),
    path('<slug:d_slug>/', views.allbranch, name='districts_by_District'),

]
