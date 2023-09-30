from products.serializer.task import TaskSerializer
from products.models.tasks import Task
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

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


class TaskList(APIView):
    """
    List all tasks, or create anew task
    """

    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(APIView):
    """
    Retrieve, update or delete a code snippet.
    """

    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        serializer = TaskSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
