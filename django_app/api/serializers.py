from django.contrib.auth.models import User
from users.models import Profile
from blog.models import Post
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['user']


class PostSerializerExplicit(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=False, max_length=100)
    date_posted = serializers.DateTimeField()

    def create(self, validated_data):
        """
        Create and return a new `Post` instance, given the validated data.
        """
        return Post.objects.create(**validated_data)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'date_posted', 'author']
