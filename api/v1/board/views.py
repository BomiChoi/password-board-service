import bcrypt
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from apps.board.models import Board
from .serializers import BoardSerializer


class BoardView(ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class BoardDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def destroy(self, request, *args, **kwargs):
        """ 비밀번호가 일치하는지 확인한 후 게시물을 삭제합니다. """
        
        post = get_object_or_404(Board, id=kwargs['pk'])
        input_pw = request.data['password'].encode('utf-8')
        pw = post.password.encode('utf-8')

        # 비밀번호가 일치하지 않을 경우
        if not bcrypt.checkpw(input_pw, pw):
            raise PermissionDenied('비밀번호가 일치하지 않습니다.')

        # 게시물 삭제
        post.delete()
        return Response(status=200)
