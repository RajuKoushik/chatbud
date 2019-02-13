from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^group/', views.group_chat, name='gc'),
    url(r'^create/group/', views.create_group, name='create_group'),
    url(r'^send/message/(?P<group_id>.+)/$', views.send_message, name='send_message'),

    url(r'^(?P<group_id>.+)/$', views.group_chat, name='group_chat'),
]
