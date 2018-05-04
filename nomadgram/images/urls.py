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
    url(
        regex=r'^(?P<image_id>[0-9]+)/unlikes/$',
        view=views.UnLikeImage.as_view(),
        name='like_image'
    ),
    # path('<int:image_id>/unlikes/', views.UnLikeImage.as_view()),
    url(
        regex=r'comments/(?P<comment_id>[0-9]+)/$',
        view=views.Comment.as_view(),
        name='comment'
    ),
    path('<int:image_id>/comments/', views.CommentOnImage.as_view()),
    url(
        regex=r'^search/$',
        views=views.Search.as_view(),
        name='search' 
    ),

]
