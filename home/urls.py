from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', views.indexHome),
   path('home', views.indexHome),
   path('contact', views.indexContact),
   path('blog', views.list),
   path('blog/<int:post_id>', views.post),
   path('register', views.register),
   path('login/', auth_views.LoginView.as_view(template_name="pages/login.html")),
   path('logout/', auth_views.LogoutView.as_view(next_page='/')),
]