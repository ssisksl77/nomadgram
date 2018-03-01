from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers


# Only for test. will not going to use it
class ListAllImages(APIView):

    def get(self, request, format=None):  # only GET HTTP

        all_images = models.Image.objects.all()
        # 시리얼라이저로 번역
        serializer = serializers.ImageSerializer(all_images, many=True)

        return Response(data=serializer.data)


class ListAllComments(APIView):

    def get(self, request, format=None):

        all_comments = models.Comment.objects.all()

        serializer = serializers.CommnetSerializer(all_comments, many=True)

        return Response(data=serializer.data)


class ListAllLikes(APIView):

    def get(self, request, format=None):

        all_likes = models.Like.objects.all()

        serializer = serializers.LikeSerializer(all_likes, many=True)

        return Response(data=serializer.data)