from django.shortcuts import render
from rest_framework import viewsets
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
# APIの処理を実装する
# CRUDの処理を書く

class CommentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDummyApiView(APIView):
    def get(self, request):
        return Response({"name": "DUMMY"})


@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)  # many=True list形式の場合はまとめて処理できるようになる引数
        return Response(serializer.data)
