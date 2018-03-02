from rest_framework import serializers
from . import models
from nomadgram.users import models as user_models


class FeedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = user_models.User
        fields = (
            'username',
            'profile_image',
        )


class CommnetSerializer(serializers.ModelSerializer):

    creator = FeedUserSerializer(read_only=True)

    class Meta:
        model = models.Comment
        fields = (
            'id',
            'message',
            'creator',
        )


class LikeSerializer(serializers.ModelSerializer):

    # image = ImageSerializer()
    class Meta:
        model = models.Like
        fields = '__all__'




class ImageSerializer(serializers.ModelSerializer):


    comments = CommnetSerializer(many=True)  # 숫자대신 실제 값이 나온다.
    # likes = LikeSerializer(many=True)
    creator = FeedUserSerializer()

    class Meta:
        model = models.Image
        fields = (
            "id",
            "file",
            "location",
            "caption",
            "creator",
            'like_count',
            "comments",  # 외래키로 엮인애들을 이렇게 불러올 수 있다. (뒤에 _set을 붙인다.)
            # "likes",
            
        )


