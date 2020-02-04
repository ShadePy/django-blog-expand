# models
from django.contrib.auth.models import User
from users.models import Profile
from blog.models import Post

# rest_framework
from rest_framework import viewsets
from .serializers import UserSerializer, ProfileSerializer, \
    PostSerializer, PostSerializerExplicit

# third-party

from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


# Test-api-views

# viewset, same as above

class PostAPIView(viewsets.ModelViewSet):
    queryset = Post.objects.order_by('date_posted')
    serializer_class = PostSerializer

# more simple with APIView

class PostAPIViewSimple(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


# rework Explicit version

# class PostViewAPIExplicit(APIView):
#     def get(self, request, *args, **kwargs):
#         queryset = Post.objects.all()
#         serializer = PostSerializerExplicit(queryset, many=True)
#         return Response(serializer.data)
#
#     @csrf_exempt
#     def post(self, request, *args, **kwargs):
#         serializer = PostSerializerExplicit(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

