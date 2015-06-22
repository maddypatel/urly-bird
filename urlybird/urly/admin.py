from django.contrib import admin
from .models import Bookmark, Click

# Register your models here.
class BookmarkAdmin(admin.ModelAdmin):
    fields = ['user', 'title', 'description', 'url', 'shorturl', 'count']
    list_display = ['title', 'url', 'shorturl']


class ClickAdmin(admin.ModelAdmin):
    class Meta:
        fields = ['bookmark', 'timestamp']
        list_display = ['bookmark', 'timestamp']


admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Click, ClickAdmin)
