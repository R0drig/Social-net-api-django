from rest_framework import serializers
from tweets.models import Tweet, Comment, Like


class LikeTweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'tweet', 'user', 'created_at')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'user', 'tweet', 'created_at')


class TweetSerializer(serializers.ModelSerializer):
    likes = LikeTweetSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True) 
    class Meta:
        model = Tweet
        fields = ('id', 'content', 'user', 'created_at','likes', 'comments',)
    