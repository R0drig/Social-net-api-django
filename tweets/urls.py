from django.urls import path
from . import views

urlpatterns = [
    path('tweet/<int:pk>/',views.TweetsViewDetail.as_view(),name='tweets_detail'),
]
