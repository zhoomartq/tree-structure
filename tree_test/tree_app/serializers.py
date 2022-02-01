from rest_framework import serializers
from .models import Worker
from rest_framework_recursive.fields import RecursiveField



class ChildrenSerializers(serializers.ModelSerializer):

    childrens = RecursiveField(many=True)
    class Meta:
        model = Worker
        fields = ('id','parent', 'fullname', 'position', 'start_date', 'salary', 'childrens')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['parent'] = instance.parent.fullname if instance.parent else None
        return representation


class WorkerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['parent'] = instance.parent.fullname if instance.parent else None
        representation['childrens'] = WorkerSerializers(instance.childrens, many=True).data
        return representation