from rest_framework import routers
from .views import *
from django.urls import path

router = routers.SimpleRouter()
router.register('user', UserViewSet)
router.register('post', PostViewSet)

urlpatterns = []

urlpatterns += router.urls
