"""urlybird URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
#from urly import views as v
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'bookmark', views.BookmarkViewSet)
router.register(r'click', views.ClickViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('^', include('django.contrib.auth.urls')),
    #url('^index$', v.index, name='index'),
    # url(r'^register$', views.user_register, name='user_register'),
    # url(r'^edit_bookmark/(?P<bookmark_id>\d*)$', views.edit_bookmark, name='edit_bookmark'),
    # url(r'^delete_bookmark/(?P<bookmark_id>\d*)$', views.delete_bookmark, name='delete_bookmark'),
    # url(r'^(?P<bookmark_id>\w{8})/?$', views.redirect_to_site, name='redirect_to_site'),
    # url(r'^shortenUrl/?$', views.shortenUrl, name='shortenUrl'),
    # #url(r'^user/(?P<user_id>\d+)$', views.user, name='user'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
]
