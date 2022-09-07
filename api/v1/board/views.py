import bcrypt
import requests
from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied
from rest_framework.exceptions import ValidationError
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from apps.board.models import Board
from .paginations import BoardPagination
from .serializers import BoardSerializer


class BoardView(ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    filter_backends = [OrderingFilter]
    ordering = ['-created_at']
    pagination_class = BoardPagination

    def perform_create(self, serializer):
        """ 현재 ip 기준 날씨 정보를 받아와서 시리얼라이저에 저장합니다. """

        url = 'https://api.weatherapi.com/v1/current.json'
        api_key = settings.API_KEY
        response = requests.get(url, params={'key': api_key, 'q': 'auto:ip'})
        if not response.ok:
            raise ValidationError('WEATHER API ERROR')

        data = response.json()
        weather_txt = data['current']['condition']['text']
        serializer.save(weather=weather_txt)


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
