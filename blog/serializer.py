from rest_framework import serializers

from blog.models import Comment, Post


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)

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

