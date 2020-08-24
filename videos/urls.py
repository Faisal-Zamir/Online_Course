from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('upload/', views.upload_form, name='upload'),
    path('video_detail/<int:id>', views.video_details, name='video_details'),



]