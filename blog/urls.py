from django.urls import path
from .views import like, postDelete, postDetail, postList, postCreate, postUpdate


app_name = "blog"
urlpatterns = [
    path('', postList, name='postlist'),
    path('postcreate/', postCreate, name='postcreate'),
    path('<str:slug>/', postDetail, name='postdetail'),
    path('<str:slug>/postupdate/', postUpdate, name='postupdate'),
    path('<str:slug>/postdelete/', postDelete, name='postdelete'),
    path('<str:slug>/postlike/', like, name='postlike'),
]