from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, CommentDummyApiView, comment_list

router = DefaultRouter()
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('dummy/', CommentDummyApiView.as_view()),
    path('list/', comment_list),
]