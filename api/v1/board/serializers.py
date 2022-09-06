from rest_framework import serializers

from apps.board.models import Board


class BoardSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = Board
        fields = (
            'id',
            'title',
            'content',
            'password',
            'created_at',
            'updated_at',
        )
