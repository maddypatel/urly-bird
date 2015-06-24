from rest_framework import serializers
from urly.models import Bookmark, Click

class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Bookmark
        fields = ('id', 'url', 'title', 'description', 'longurl', 'shorturl', 'user')


class ClickSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Click
        fields = ('id', 'user', 'bookmark')



