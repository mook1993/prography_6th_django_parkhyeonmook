"""Urls of usersurvey."""
from django.conf.urls import url,include
from django.urls import path
from rest_framework import routers
from .views import Board_List_API, Board_API

list = {
    'get': 'list',
}

router = routers.DefaultRouter()
router.register('article', Board_API) # prefix = movies , viewset = MovieViewSet


urlpatterns = [
    path('article_list/', Board_List_API.as_view(list), name='article_list'),
    url(r'^', include(router.urls)),
]