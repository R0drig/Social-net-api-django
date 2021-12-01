from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.http import Http404

from .models import Tweet
from .serializers import TweetSerializer

class TweetsViewDetail(APIView):
  """ 
  A view that returns the detailed view of a tweet
  """
  permission_classes = [AllowAny]
  def get_object(self, pk):
    try:
      return Tweet.objects.get(pk=pk)
    except Tweet.DoesNotExist:
      raise Http404
  
  def get(self, request, pk, format=None):
    tweet = self.get_object(pk)
    serializer = TweetSerializer(tweet)
    return Response(serializer.data)
      