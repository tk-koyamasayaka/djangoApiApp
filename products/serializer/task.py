from rest_framework import serializers
from products.models.tasks import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['content', 'due_date']

        """
        >>> from products.serializer.task import TaskSerializer
        >>> serializer = TaskSerializer()
        >>> print(repr(serializer))
        
        ModelSerializerクラスは特に魔法のようなことをするわけではなく、シリアライザー クラスを作成するための単なるショートカットであることを覚えておくことが重要
        """