from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views import PostListApiView, PostAddApiView, PostDestroyAPIView, PostUpdateAPIView, CommentModelViewSet, \
    CustomFormApiView

router = DefaultRouter()
# router.register(r'comment', CommentModelViewSet, 'comment')
'''
comment-list        comment/    GET
comment-add         comment/    POST
comment-retrieve    comment/id  GET
comment-update      comment/id  PATCH, PUT
comment-destroy     comment/id  DELETE

comment/4

'''
urlpatterns = [
    # path('', include(router.urls)),

    # path('post-list', PostListApiView.as_view(), name='post-list'),
    path('post-add', PostAddApiView.as_view(), name='post-add'),
    # path('post-delete/<int:pk>', PostDestroyAPIView.as_view(), name='post-delete'),
    # path('post-update/<int:pk>', PostUpdateAPIView.as_view(), name='post-update'),
    path('form', CustomFormApiView.as_view())
]
