from products.serializer.task import TaskSerializer
from products.models.tasks import Task
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

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


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'tasks': reverse('tasks-list', request=request, format=format)
    })


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
