from django.contrib.auth.models import User
from rest_framework import serializers
from ApiDataLab.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES, OpinionPoll

#Esto es para poder navegar a travez de la api

class SnippetSerializerHiper(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style')


class UserSerializerHiper(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'snippets')

class AutorSerializer(serializers.Serializer):
    class Meta:
        fields = ('forum_name', 'subject', 'answered', 'last_post_datetime', 'replies', 'tags', 'views')

    forum_name = serializers.CharField(max_length=200)
    subject = serializers.CharField(max_length=200)
    answered = serializers.IntegerField(max_value=1000)
    last_post_datetime = serializers.CharField(max_length=200)
    replies = serializers.IntegerField(max_value=1000)
    tags = serializers.ListField(child=serializers.CharField(max_length=200))
    views = serializers.IntegerField(max_value=1000)