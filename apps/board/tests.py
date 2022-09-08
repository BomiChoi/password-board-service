import bcrypt
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Board


class TestBoard(APITestCase):
    def setUp(self):
        """ Test 시작 전 필요한 임시 데이터 생성 """
        # 비밀번호 암호화
        password = 'test01'
        encoded_pw = password.encode('utf-8')
        hashed_pw = bcrypt.hashpw(encoded_pw, bcrypt.gensalt())
        decoded_pw = hashed_pw.decode('utf-8')

        # 게시물 생성
        self.board_url = "/api/v1/posts"
        self.post_id = 1
        self.post = Board.objects.create(
            id=self.post_id,
            title='test01',
            content='test01',
            password=decoded_pw
        )

    def tearDown(self):
        """ Test를 위해 생성했던 임시 데이터 삭제 """
        Board.objects.all().delete()

    def test_create_post_success(self):
        """ 게시물 작성 성공 """
        data = {
            'title': 'test02',
            'content': 'test02',
            'password': 'test02'
        }
        self.response = self.client.post(self.board_url, data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_create_post_fail_1(self):
        """ 게시물 작성 실패 (비밀번호 길이 6자 미만) """
        data = {
            'title': 'test02',
            'content': 'test02',
            'password': 'test1'
        }
        self.response = self.client.post(self.board_url, data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_post_fail_2(self):
        """ 게시물 작성 실패 (비밀번호 숫자 미포함) """
        data = {
            'title': 'test02',
            'content': 'test02',
            'password': 'testtest'
        }
        self.response = self.client.post(self.board_url, data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_post_success(self):
        """ 게시물 목록 조회 성공 """
        self.response = self.client.get(f'{self.board_url}')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_retrieve_post_success(self):
        """ 게시물 조회 성공 """
        self.response = self.client.get(f'{self.board_url}/{self.post_id}')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_update_post_success(self):
        """ 게시물 수정 성공 """
        data = {
            'title': 'test02',
            'content': 'test02',
            'password': 'test01'
        }
        self.response = self.client.put(f'{self.board_url}/{self.post_id}', data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_update_post_fail(self):
        """ 게시물 수정 실패 (비밀번호 불일치) """
        data = {
            'title': 'test02',
            'content': 'test02',
            'password': 'test02'
        }
        self.response = self.client.put(f'{self.board_url}/{self.post_id}', data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_post_success(self):
        """ 게시물 삭제 성공 """
        data = {
            'password': 'test01'
        }
        self.response = self.client.delete(f'{self.board_url}/{self.post_id}', data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_delete_post_fail(self):
        """ 게시물 삭제 실패 (비밀번호 불일치) """
        data = {
            'password': 'test02'
        }
        self.response = self.client.delete(f'{self.board_url}/{self.post_id}', data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
