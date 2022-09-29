from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo

@api_view(["GET"])
def todolist(req):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def todocreate(req):
    serializer = TodoSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.error)

@api_view(["PUT"])
def todoupdate(req,pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(todo, data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.error)

@api_view(["DELETE"])
def tododelete(req,pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return Response("삭제되었습니다.")