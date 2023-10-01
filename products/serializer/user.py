from django.contrib.auth.models import User
from rest_framework import serializers
from products.models import Task


class UserSerializer(serializers.ModelSerializer):
    # 他の型付きフィールドとは対照的に、型なしクラスです。型なしは常に読み取り専用であり、シリアル化された表現に使用されますが、モデルの更新には使用されません
    tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'tasks']
