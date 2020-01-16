from rest_framework.serializers import HyperlinkedModelSerializer
from ghostpostrestapi.models import GhostPost


class PostSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = GhostPost
        fields = ['is_boast',
                  'content',
                  'upvotes',
                  'downvotes',
                  'post_date',
                  'net_votes', 
                  'id']