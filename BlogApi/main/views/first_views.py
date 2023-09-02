from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..serializers import PostSerializer
from ..models import Post


class BookApiView(APIView):

    queryset = Post.objects.all()

    def get(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
