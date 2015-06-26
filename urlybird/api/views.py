from urly.models import Bookmark, Click
from api.serializers import BookmarkSerializer, ClickSerializer, ClickWithBookmarkSerializer, UserSerializer
from rest_framework import viewsets, permissions, generics, filters
from api.permissions import IsOwnerOrReadOnly, IsUser
from rest_framework.exceptions import PermissionDenied
from django.db.models import Count
from django.contrib.auth.models import User


class BookmarkViewSet(viewsets.ModelViewSet):
    serializer_class = BookmarkSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrReadOnly)

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user).annotate(
            click_count=Count('click', distinct=True))

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ClickViewSet(viewsets.ModelViewSet):
    queryset = Click.objects.all()
    serializer_class = ClickSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ClickCreateView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ClickSerializer

    def initial(self, request, *args, **kwargs):
        self.bookmark = Bookmark.objects.get(pk=kwargs['bookmark_pk'])
        super().initial(request, *args, **kwargs)

    def get_queryset(self):
        return self.bookmark.click_set.all()

    def perform_create(self, serializer):
        if self.request.user != self.bookmark.user:
            raise PermissionDenied
        serializer.save(bookmark=self.bookmark)


class ClickDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ClickWithBookmarkSerializer
    queryset = Click.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
