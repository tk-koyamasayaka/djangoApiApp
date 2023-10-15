import re

from rest_framework import serializers
from products.models.tasks import Task


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = ['content', 'due_date', 'owner']

        """
        >>> from products.serializer.task import TaskSerializer
        >>> serializer = TaskSerializer()
        >>> print(repr(serializer))
        
        ModelSerializerクラスは特に魔法のようなことをするわけではなく、シリアライザー クラスを作成するための単なるショートカットであることを覚えておくことが重要
        """

    def validate_content(self, value):
        pattern = re.compile(r"フガ|ホゲ")
        if pattern.search(value):
            raise serializers.ValidationError("投稿不可の単語が含まれています")
        return value

