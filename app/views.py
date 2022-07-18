from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from app.serializers import PostSerializers, CommentSerializer, FormSerializers

from app.models import Posts, Comment


class PostListApiView(ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializers


class PostAddApiView(CreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializers


class PostDestroyAPIView(DestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializers
    lookup_url_kwarg = 'pk'


class PostUpdateAPIView(UpdateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializers
    lookup_url_kwarg = 'pk'


class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CustomFormApiView(APIView):
    parser_classes = (MultiPartParser, FileUploadParser)
    http_method_names = ['post', 'get',]

    def delete(self):
        return Response({'status': 'deleted'})

    def get(self, request, format=None):
        return Response({'status': True})

    def post(self, request, format=None):
        serializer_data = FormSerializers(data=self.request.data)
        serializer_data.is_valid(raise_exception=True)
        return Response(serializer_data.data)