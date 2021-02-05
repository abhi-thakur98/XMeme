from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('memes/',views.MemeList.as_view(),name='memes'),
    path('owners/',views.OwnerList.as_view(),name='owner'),
    path('memes/<int:pk>',views.MemeDetails.as_view(),name='meme-details'),
    path('owners/<int:pk>',views.OwnerDetails.as_view(),name='owner-details'),
]