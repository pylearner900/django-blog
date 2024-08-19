from django.urls import path
from .views import index,PostView,CreatePost,UpdatePost,DeletePost

urlpatterns = [
    path("",index,name='index'),
    path("post/<int:pk>/",PostView.as_view(),name='postview'),
    path("createPost/",CreatePost.as_view(),name="createPost"),
    path("updatePost/<int:pk>",UpdatePost.as_view(),name="updatePost"),
    path("deletePost/<int:pk>",DeletePost.as_view(),name="deletePost"),
    
]