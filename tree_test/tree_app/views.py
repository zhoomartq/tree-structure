from .serializers import ChildrenSerializers, WorkerSerializers
from .models import Worker
from rest_framework import viewsets, mixins, decorators, status
from rest_framework.response import Response




class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializers


    @decorators.action(detail=False, methods=['get'])
    def tree(self, *args, **kwargs):
        workers = Worker.objects.filter(id=1).all()
        serializer = ChildrenSerializers(workers, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

