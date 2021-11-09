from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .serializers import *
from rest_framework.filters import SearchFilter, OrderingFilter
from .services import *

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['nickname', 'registration_date']
    ordering_fields = ['nickname', 'registration_date']

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['author', 'title', 'post_date_time']
    ordering_fields = ['author', 'title', 'post_date_time']
