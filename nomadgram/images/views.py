from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers


class Feed(APIView):

    def get(self, request, format=None):
        user = request.user
        print('current user::: ', user)

        following_users = user.following.all()

        image_list = []
        for following_user in following_users:
            user_images = following_user.images.all()[:2]
            for image in user_images:
                image_list.append(image)

        sorted_list = sorted(image_list, key=lambda image: image.created_at, reverse=True)

        serializer = serializers.ImageSerializer(sorted_list, many=True)

        return Response(serializer.data)


class LikeImage(APIView):

    def post(self, request, image_id, format=None):

        user = request.user
        try:
            found_image = models.Image.objects.get(id=image_id)  # get | filter | all
        except models.Image.DoesNotExist as e:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            preexisting_like = models.Like.objects.get(
                creator=user,
                image=found_image
            )
            return Response(status=status.HTTP_304_NOT_MODIFIED)
        except models.Like.DoesNotExist:
            new_like = models.Like.objects.create(
                creator=user,
                image=found_image
            )
            new_like.save()
            return Response(status=status.HTTP_201_CREATED)  # return Response(status=200)


class UnLikeImage(APIView):

    def delete(self, request, image_id, format=None):
        user = request.user
        try:
            found_image = models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            preexisting_like = models.Like.objects.get(
                creator=user,
                image=found_image
            )
            preexisting_like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except models.Like.DoesNotExist:
            return Response(status=status.HTTP_304_NOT_MODIFIED)
        

class CommentOnImage(APIView):

    def post(self, request, image_id, format=None):
        user = request.user
        res = None
        try:
            found_image = models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            res = {'status': status.HTTP_404_NOT_FOUND}
        else:
            serializer = serializers.CommnetSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save(creator=user, image=found_image)
                res = {'data': serializer.data, 'status': status.HTTP_200_OK}
            else:
                res = {'data': serializer.errors, 'status': status.HTTP_400_BAD_REQUES}

        return Response(**res)


class Comment(APIView):
    def delete(self, request, comment_id, format=None):
        user = request.user

        try:
            comment = models.Comment.objects.get(id=comment_id, creator=user)
            comment.delete()
            res = {'status': status.HTTP_204_NO_CONTENT}
        except models.Comment.DoesNotExist:
            res = {'status': status.HTTP_404_NOT_FOUND}

        return Response(**res)
