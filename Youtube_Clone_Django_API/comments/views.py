from django.shortcuts import render
from rest_framework import serializers
from rest_framework.serializers import Serializer
from .models import Comment
from .models import Reply
from .serializers import CommentSerializer
from .serializers import ReplySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http.response import Http404
# Create your views here.


class CommentList(APIView):

    def get(self,request):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CommentDetail(APIView):
    def get_object(self,pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404
    
    def get(self,request,pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)


    def put(self,request,pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentVideo(APIView):
    def get_object(self,pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404
    
    def get(self,request,video_Id):
        comment = Comment.objects.filter(video=video_Id)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)



class ReplyList(APIView):
    def get(self,request):
        reply = Reply.objects.all()
        serializer = ReplySerializer(reply, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ViewReply(APIView):
    def get_object(self,pk):
        try:
            return Reply.objects.get(pk=pk)
        except Reply.DoesNotExist:
            raise Http404
    
    def get(self,request, comment_Id):
        reply = Reply.objects.filter(comment_id_id=comment_Id)
        serializer = ReplySerializer(reply, many=True)
        return Response(serializer.data)

