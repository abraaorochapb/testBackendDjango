from django.urls import path
from .views import PostsViewSet

urlpatterns = [
    path('posts/', PostsViewSet.as_view()),
    path('posts/<int:id>/', PostsViewSet.as_view())
]