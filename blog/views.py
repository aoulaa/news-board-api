from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Post, Upvote, Comment
from blog.serializer import PostSerializer, CommentSerializer, UpvoteSerializer


class PostListView(APIView):
    def get(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, 201)


class PostDetailView(APIView):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response({}, 204)


class Vote(APIView):
    def post(self, request, postId, userId):
        # userId = request.user.userID
        current_upvote = Upvote.objects.filter(voter=userId, post=postId).first()
        if not current_upvote:
            new_upvote = {"voter": userId, "post": postId}
            serializer = UpvoteSerializer(data=new_upvote)
            if serializer.is_valid():
                serializer.save()
                return Response("voted", status=status.HTTP_200_OK)
        return Response("Already upvoted", status=status.HTTP_200_OK)


class CommentListView(APIView):
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, 201)


class CommentDetailView(APIView):
    def get(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        serializer = CommentSerializer(comment, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()
        return Response({}, 204)
