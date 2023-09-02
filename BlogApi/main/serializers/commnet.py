from rest_framework import serializers

from ..models import Comments

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = ['id', 'user', "post_id", "text",]


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'user', "post_id", "text",]


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id','user', "post_id", "text" ]


class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['text']

