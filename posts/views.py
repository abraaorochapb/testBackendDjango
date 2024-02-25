from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.views import APIView  
from rest_framework.response import Response
from rest_framework import status

class PostsViewSet(APIView):  
    def get(self, request, id=None):  
        if id:
            post = get_object_or_404(models.Post, id=id)  
            serializer = serializers.PostSerializer(post)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
        posts = models.Post.objects.all()
        serializer = serializers.PostSerializer(posts, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = serializers.PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        post = get_object_or_404(models.Post, id=id)
        serializer = serializers.PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id=None):
        post = get_object_or_404(models.Post, id=id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)