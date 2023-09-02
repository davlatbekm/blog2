from rest_framework.decorators import action
from rest_framework.generics import mixins
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ..models import Post, Comments
from ..serializers import PostSerializer, PostCreateSerializer, PostUpdateSerializer, CommentCreateSerializer, CommentUpdateSerializer, CommentSerializer



class PostGenericApiView(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if (self.action == "list"):
            return PostSerializer
        if (self.action == "create"):
            return PostCreateSerializer
        if (self.action == "patch"):
            return PostUpdateSerializer
        return PostSerializer


class CommentGenericApiView(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    permission_classes = [AllowAny]
    queryset = Comments.objects.all()

    def get_serializer_class(self):
        if (self.action == "list"):
            return CommentSerializer
        if (self.action == "create"):
            return CommentCreateSerializer
        if (self.action == "patch"):
            return CommentUpdateSerializer
        return CommentSerializer

