from urly.models import Bookmark, Click
from api.serializers import BookmarkSerializer, ClickSerializer
from rest_framework import viewsets, permissions, generics
from api.permissions import IsOwnerOrReadOnly, OwnsRelatedBookmark
from rest_framework.exceptions import PermissionDenied

class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ClickViewSet(viewsets.ModelViewSet):
    queryset = Click.objects.all()
    serializer_class = ClickSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ClickCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ClickSerializer

    def perform_create(self, serializer):
        bookmark = serializer.validated_data['bookmark']
        if self.request.user != bookmark.user:
            raise PermissionDenied
        serializer.save()