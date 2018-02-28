from django.db import models
from nomadgram.users import models as user_models
from django.utils.encoding import python_2_unicode_compatible


# abstract 클래스는 데이터베이스와 직접연결되지 않는다.
@python_2_unicode_compatible
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return 

    def __unicode__(self):
        return 


@python_2_unicode_compatible
class Image(TimeStampedModel):
    """
    Image Model
    """
    file = models.ImageField()
    location = models.CharField(max_length = 140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.location, self.caption)


@python_2_unicode_compatible
class Comment(TimeStampedModel):
    """
    Comment Model
    """
    message = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.message


@python_2_unicode_compatible
class Like(TimeStampedModel):
    """
    Like Model
    """
    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return 'User: {} - Image Caption: {}'.format(self.creator.username, self.image.caption)