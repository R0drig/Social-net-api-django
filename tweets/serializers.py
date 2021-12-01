from rest_framework import serializers
from tweets.models import Tweet, Comment, Like
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
          'id',
          'username',)

class LikeTweetSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Like
        fields = ('id', 'tweet', 'user', 'created_at')


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'content', 'user', 'tweet', 'created_at')


class TweetSerializer(serializers.ModelSerializer):
    likes = LikeTweetSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True) 
    user = UserSerializer(read_only=True)
    class Meta:
        model = Tweet
        fields = ('id', 'user','content' , 'created_at','likes', 'comments',)
    