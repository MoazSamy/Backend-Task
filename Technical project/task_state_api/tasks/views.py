from django.shortcuts import render
from rest_framework import generics , status
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer
from django.http import Http404
from rest_framework.response import Response

# List of all the present tasks
class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# CRUD view of a single task
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskAdvance(APIView):

    # 
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk,):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        if not task.nextState():
            return Response({"msg":"This task is already archived , can't advance anymore"} , status=status.HTTP_400_BAD_REQUEST)
        task.save()
        return Response(serializer.data)

class TaskArchive(APIView):

    #
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk,):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        if task.state == "ARCH":
            return Response({"msg" : "This task is already archived , can't advance anymore" } , status=status.HTTP_400_BAD_REQUEST)
        else:
            task.state = "ARCH"
        task.save()
        return Response(serializer.data)