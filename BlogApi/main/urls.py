from django.urls import path, include
from rest_framework import routers
from .views import PostGenericApiView, CommentGenericApiView

router = routers.DefaultRouter()
router.register("post", PostGenericApiView, "generic")
router.register("comments", CommentGenericApiView, "generic")


urlpatterns = [
    path('', include(router.urls)),

]
