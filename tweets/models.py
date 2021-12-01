from django.db import models
from accounts.models import User
# Create your models here.

class Tweet(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets')
  content = models.CharField(max_length=140)
  image = models.FileField(upload_to="uploads/",blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return f'{self.user} - {self.content}'
  
class Like(models.Model):
  tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='likes')
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
  like = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  

class Comment(models.Model):
  tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='comments')
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
  content = models.CharField(max_length=140)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return f'{self.user} - {self.tweet} - {self.content}'
  
  
  