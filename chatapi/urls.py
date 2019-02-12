from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^group/', views.group_chat, name='gc'),
    url(r'^(?P<group_id>.+)/$', views.group_chat, name='group_chat'),

]
