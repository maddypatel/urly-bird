from django.db import models
from django.contrib.auth.models import User
from faker import Factory
import random, string

# Create your models here.


class Bookmark(models.Model):
    user = models.ForeignKey(User, related_name="urly")
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    longurl = models.URLField()
    shorturl = models.CharField(max_length=8)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.shorturl


class Click(models.Model):
    user = models.ForeignKey(User)
    bookmark = models.ForeignKey(Bookmark)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.timestamp)


def create_user():
    for i in range(1, 21):
        user = User.objects.create_user(
            "user{}".format(i),
            "user{}@theironyard.com".format(i),
            "user{}".format(i)
        )
        user.save()


def create_bookmarks():
    fake = Factory.create()
    for user in User.objects.all():
        for _ in range(10):
            title = fake.word()
            description = fake.sentence(nb_words=4)
            longurl = fake.url()
            shorturl = generate_shorturl()
            time_created = fake.date_time_this_month()
            #count = random.randrange(1, 51)
            bookmark = Bookmark(user=user, title=title, description=description, longurl=longurl, shorturl=shorturl,
                                time_created=time_created)
            bookmark.save()


def create_clicks():
    fake = Factory.create()
    for bookmark in Bookmark.objects.all():
        user = random.choice(User.objects.all())
        timestamp = fake.date_time_this_month()
        click = Click(user=user, bookmark=bookmark, timestamp=timestamp)
        click.save()


def generate_shorturl():
    rand_char = string.ascii_letters + string.digits
    unique_code = ''.join(random.choice(rand_char) for i in range(8))
    return unique_code
