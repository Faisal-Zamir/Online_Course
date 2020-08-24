from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.BlogHome, name='blog-home'),
    path('post-form', views.BlogForm, name='post-form'),
    path('post-details/<int:id>', views.PostDetails, name='post-details'),

]
