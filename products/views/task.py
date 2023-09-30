from products.serializer.task import TaskSerializer
from products.models.tasks import Task
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status

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


@api_view(['GET', 'POST'])
def task_list(request):
    """
    List all conde Tasks, or create or new task.
    """
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
def task_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TaskSerializer(task)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = TaskSerializer(task, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

    elif request.method == "DELETE":
        task.delete()
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
