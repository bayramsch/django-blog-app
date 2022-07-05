from django.urls import path
from django.contrib.auth import views as auth_views
from .views import profile, register, user_login, user_logout
from .forms import PasswordResetEmailCheck

app_name = "users"
urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name="logout"),
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name="users/password_reset_email.html", form_class=PasswordResetEmailCheck), name="password_reset"),
] 