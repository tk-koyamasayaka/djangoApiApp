from products.serializer.task import TaskSerializer
from products.models.tasks import Task
from rest_framework import generics, permissions

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


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    """
    REST フレームワークには、特定のビューにアクセスできるユーザーを制限するために使用できる多数の権限クラスが含まれている
    今回はIsAuthenticatedOrReadOnlyを設定しており、これは認証されたリクエストは読み取り/書き込みアクセスが取得され、
    認証されていないリクエストは読み取り専用アクセスが取得可能となる。
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
