from products.serializer.task import TaskSerializer
from products.models.tasks import Task
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics

# Create your views here.
# リクエストを受け取り、適切なレスポンスを生成する役割
# HTTPリクエスト取得 → （何らかの処理）→ HTTPレスポンス返却
# CRUDの処理を書く

"""
REST フレームワークには、API ビューの作成に使用できる 2 つのラッパーが用意されている
1. 関数ベースのビューを操作するためのデコレータ@api_view
2. APIViewクラスベースのビューを操作するためのクラス

ラッパーは、405 Method Not Allowed適切な場合に応答を返したり、
不正な入力でParseErrorアクセスしたときに発生する例外を処理したりするなどの動作も提供する
"""


class TaskList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """
    List all tasks, or create anew task
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TaskDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    """
    Retrieve, update or delete a code snippet.
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request,  *args, **kwargs)

    def put(self, request,  *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request,  *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
