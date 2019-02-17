import django.contrib.auth.views as auth_views
from django.conf.urls import url, include
from django.views.generic.base import RedirectView

from . import views

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    # url(r'^$', views.index, name='index'),

    url(r'^oauth/', include('social_django.urls', namespace='social')),

    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^favicon\.ico$', favicon_view),
    url(r'^homy/', views.homy, name='homy'),

    url(r'^$', views.home, name='home'),
    # url(r'^(?P<room_name>.+)/$', views.room, name='room'),
    url(r'^group/', views.group_chat, name='gc'),
    url(r'^create/group/', views.create_group, name='create_group'),
    url(r'^send/message/(?P<group_id>.+)/$', views.send_message, name='send_message'),

    url(r'^(?P<group_id>.+)/$', views.group_chat, name='group_chat'),
]
