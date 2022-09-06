from django.urls import path, include

urlpatterns = [
    path('/posts', include('api.v1.board.urls')),
]
