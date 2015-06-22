from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm, EditForm, BookmarkForm
from .models import Bookmark
from django.contrib import messages
import random
import string


# Create your views here.
def user_register(request):
    if request.method == "GET":
        user_form = UserForm()
    elif request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            password = user.password
            user.set_password(password)
            user.save()
            user = authenticate(username=user.username,
                                password=password)
            login(request, user)

            return redirect('index')
    return render(request, "urly/register.html",
                  {'user_form': user_form})


def index(request):
    bookmarks = Bookmark.objects.all()
    return render(request,
                  "urly/index.html",
                  {"bookmarks": bookmarks})


def edit_bookmark(request, bookmark_id):
    bookmark = Bookmark.objects.get(pk=bookmark_id)
    if request.method == "POST":
        edit_form = EditForm(request.POST, instance=bookmark)
        if edit_form.is_valid():
            new_bookmark = edit_form.save(commit=False)
            new_bookmark.url = bookmark
            new_bookmark.save()
            messages.add_message(request, messages.SUCCESS,
                                 "You have successfully changed the bookmark.")

        return redirect('edit_bookmark', request.user.id)
    else:
        edit_form = EditForm(instance=bookmark)
    return render(request,
                  'urly/edit_bookmark.html',
                  {'edit_form': edit_form,
                   'bookmark': bookmark})


def delete_bookmark(request, bookmark_id):
    bookmark = Bookmark.objects.get(pk=bookmark_id)
    if request.method == "POST":
        messages.add_message(request, messages.SUCCESS,
                             "You have successfully deleted the bookmark.")

        bookmark.delete()
        return redirect('index', request.user.id)

    return render(request,
                  'urly/delete.html',
                  {'bookmark': bookmark})


def redirect_to_site(request, bookmark_id):
    short = Bookmark.objects.get(pk=bookmark_id)
    short.count += 1
    short.save()
    return redirect(short.url)


def shortenUrl(request):
    rand_char = string.ascii_letters + string.digits
    unique_code = ''.join(random.choice(rand_char) for i in range(8))

    if request.method == "POST":
        form = BookmarkForm(request.POST)
        if form.is_valid():
            short = form.save(commit=False)
            short.shorturl = unique_code
            short.save()

            return redirect('shortenUrl', request.user.id)

    else:
        form = BookmarkForm()

    return render(request,
                  'urly/shortenUrl.html',
                  {'form': form})
