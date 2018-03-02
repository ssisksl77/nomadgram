from django.conf.urls import url
from django.urls import path
from . import views


app_name = 'images'
urlpatterns = [
    url(
        regex=r'^$',
        view=views.Feed.as_view(),
        name='feed'
    ),
    url(
        regex=r'^(?P<image_id>[0-9]+)/likes/$',
        view=views.LikeImage.as_view(),
        name='like_image'
    ),
    # url(
    #    regex=r'^(?P<image_id>[0-9]+)/comments/$',
    #    view=views.CommentOnImage.as_view(),
    #    name='comment_image'
    # ),
    # 두가지 방법이 있음.
    path('<int:image_id>/comments/', views.CommentOnImage.as_view()),
    url(
        regex=r'comments/(?P<comment_id>[0-9]+)/$',
        view=views.Comment.as_view(),
        name='comment'
    )
]
