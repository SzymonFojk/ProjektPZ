from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('home/', views.home, name='portal-home'),
    path('about/', views.about, name='portal-about'),
    path('register/', user_views.register, name='register'),
    path('profile/<str:username>/', user_views.profile, name='profile'),
    path('profile/', user_views.profile, name='profile'),
    path('connect/<str:operation>/<int:user_id>/', user_views.make_friends, name='connect'),
    path('', auth_views.LoginView.as_view(template_name='users/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/login.html'), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
