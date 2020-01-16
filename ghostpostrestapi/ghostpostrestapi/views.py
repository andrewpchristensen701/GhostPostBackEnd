from rest_framework import viewsets

from ghostpostrestapi.models import GhostPost
from ghostpostrestapi.serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


class PostView(viewsets.ModelViewSet):
    queryset = GhostPost.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['get'])
    def upvote(self, request, pk=None):
        like = GhostPost.objects.get(pk=pk)
        like.net_votes += 1
        like.save()
        return Response({'status': 'liked!'})

    @action(detail=True, methods=['get'])
    def downvote(self, request, pk=None):
        like = GhostPost.objects.get(pk=pk)
        like.net_votes -= 1
        like.save()
        return Response({'status': 'disliked!'})