from rest_framework import serializers
from blog.models import Comment, Post, Upvote


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "id",
            "commenter",
            "content",
            "created_at",
            "post"
        ]


class UpvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upvote
        fields = [
            "id",
            "voter",
            'post'
        ]


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)
    upvote = UpvoteSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "link",
            "created_at",
            "author_name",
            "upvote",
            "comments",
        )


