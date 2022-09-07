import bcrypt
from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied, ValidationError

from apps.board.models import Board


class BoardSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6, max_length=20, style={'input_type': 'password'})
    weather = serializers.CharField(read_only=True, max_length=20, required=False, allow_null=True)

    class Meta:
        model = Board
        fields = (
            'id',
            'title',
            'content',
            'password',
            'created_at',
            'updated_at',
            'weather',
        )

    def validate(self, attrs):
        """ 비밀번호를 검증합니다. """

        if not any(c.isdigit() for c in attrs['password']):
            raise ValidationError({'password', '비밀번호는 숫자를 1개 이상 포함해야 합니다.'})
        return attrs

    def create(self, validated_data):
        """ 비밀번호를 암호화한 후 게시물을 생성합니다. """

        # 비밀번호 암호화
        pw = validated_data.pop('password').encode('utf-8')
        hashed_pw = bcrypt.hashpw(pw, bcrypt.gensalt())
        decoded_pw = hashed_pw.decode('utf-8')

        # 게시물 생성
        post = Board.objects.create(password=decoded_pw, **validated_data)
        return post

    def update(self, instance, validated_data):
        """ 비밀번호가 일치하는지 확인한 후 게시물을 수정합니다. """

        input_pw = validated_data['password'].encode('utf-8')
        pw = instance.password.encode('utf-8')

        # 비밀번호가 일치하지 않을 경우
        if not bcrypt.checkpw(input_pw, pw):
            raise PermissionDenied('비밀번호가 일치하지 않습니다.')

        # 게시물 수정
        instance.title = validated_data['title']
        instance.content = validated_data['content']
        instance.save()
        return instance
