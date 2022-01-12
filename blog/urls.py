from django.urls import path
from blog.views import (
    PostListView,
    PostDetailView,
    CommentListView,
    CommentDetailView,
    Vote,
)

urlpatterns = [
    path("post", PostListView.as_view(), name="post-list"),
    path("post/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("post/vote/<int:postId>/<int:userId>", Vote.as_view(), name="vote"),
    path("comment", CommentListView.as_view(), name="comment-list"),
    path("comment/<int:pk>", CommentDetailView.as_view(), name="comment-detail"),
]
