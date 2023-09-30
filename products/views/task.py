from rest_framework import generics
from products.serializer.task import TaskSerializer
from products.models.tasks import Task
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


# Create your views here.
# リクエストを受け取り、適切なレスポンスを生成する役割
# HTTPリクエスト取得 → （何らかの処理）→ HTTPレスポンス返却
# CRUDの処理を書く

@csrf_exempt
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
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def task_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse(status=404)

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
        return HttpResponse(status=404)

