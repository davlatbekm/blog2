from rest_framework import serializers

from ..models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', "user", "image", "description",]


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', "user", "image", "description",]


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', "user", "image", "description", ]


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["image", "description"]

