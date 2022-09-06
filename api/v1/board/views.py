from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.board.models import Board
from .serializers import BoardSerializer


class BoardView(ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class BoardDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
