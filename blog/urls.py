from django.urls import path
from blog.views import PostListView, PostDetailView, vote_view, CommentListView, CommentDetailView

urlpatterns = [
    path('post', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/vote', vote_view, name='vote-view'),
    path('comment', CommentListView.as_view(), name='comment-list'),
    path('comment/<int:pk>', CommentDetailView.as_view(), name='comment-detail'),

]
