from django.db import models
from django.contrib.auth.models import User
from faker import Factory
import random

# Create your models here.


class Bookmark(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    url = models.URLField()
    shorturl = models.CharField(max_length=8)
    time_created = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.shorturl


class Click(models.Model):
    bookmark = models.ForeignKey(Bookmark)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.timestamp)


def create_user():
    for i in range(50):
        user = User.objects.create_user(
            "user{}".format(i),
            "user{}@theironyard.com".format(i),
            "user{}".format(i)
        )
        user.save()


def create_bookmarks():
    fake = Factory.create()
    for user in User.objects.all():
        for _ in range(20):
            title = fake.word()
            description = fake.sentence(nb_words=4)
            url = fake.url()
            time_created = fake.date_time_this_month()
            count = random.randrange(1, 51)
            bookmark = Bookmark(user=user, title=title, description=description, url=url, time_created=time_created,
                                count=count)
            bookmark.save()


def create_clicks():
    fake = Factory.create()
    for bookmark in Bookmark.objects.all():
        for _ in range(bookmark.count):
            timestamp = fake.date_time_this_month()
            click = Click(bookmark=bookmark, timestamp=timestamp)
            click.save()
