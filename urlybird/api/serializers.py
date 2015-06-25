from rest_framework import serializers
from urly.models import Bookmark, Click
from rest_framework.fields import SerializerMethodField
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from rest_framework import serializers


class ClickSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Click
        fields = ('id', 'user', 'bookmark')


class ClickWithBookmarkSerializer(serializers.HyperlinkedModelSerializer):
    bookmark = serializers.HyperlinkedRelatedField(read_only=True,
                                                   view_name='click-detail')

    class Meta:
        model = Click
        fields = ('id', 'url', 'bookmark')


class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    clicks = ClickSerializer(many=True, read_only=True)
    click_count = serializers.IntegerField(read_only=True)
    _links = SerializerMethodField()

    def get__links(self, obj):
        links = {
            "clicks": reverse('click-list', kwargs=dict(bookmark_pk=obj.pk),
                              request=self.context.get('request'))}
        return links

    class Meta:
        model = Bookmark
        fields = ('id', 'url', 'title', 'description', 'longurl', 'shorturl', 'user', 'clicks', 'click_count', '_links')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'password', 'email')
        write_only_fields = ('password',)

        def create(self, validated_data):
            user = User.objects.create(
                username = validated_data['username'],
                email = validated_data['email']
            )

            user.set_password(validated_data['password'])
            user.save()

            return user