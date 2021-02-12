from django.urls import path
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

from . import views

schema_view = get_swagger_view(title='API Documentation')
urlpatterns = [
    url(r'^api/$', schema_view),
    path('', views.index, name='index'),
    path('memes',views.MemeList.as_view(),name='memes'),
    path('owners',views.OwnerList.as_view(),name='owner'),
    path('memes/<int:pk>',views.MemeDetails.as_view(),name='meme-details'),
    path('owners/<int:pk>',views.OwnerDetails.as_view(),name='owner-details'),
]