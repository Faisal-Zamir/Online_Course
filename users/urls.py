from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('user_profiles/', views.user_profiles , name="user_profiles"),
    path('subscribed_videos/', views.subscribed_videos , name="subscribed_videos"),

    path('subscribe/<int:pk>', views.subscribe, name='subscribe'),
    path('unsubscribe/<int:pk>', views.unsubscribe, name='unsubscribe'),
    path('logout/', views.user_logout , name="logout"),

]
