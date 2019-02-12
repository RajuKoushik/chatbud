from django.contrib.auth.models import User
from django.db import models


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(default=0)
    join_date = models.DateTimeField('Join published', default='2011-11-11 11:11')

    def __str__(self):
        return self.user.first_name


class Group(models.Model):
    title = models.TextField(max_length=420)
    description = models.TextField(max_length=420)
    admin = models.ForeignKey(
        User, related_name='admin', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'


class Message(models.Model):
    content = models.TextField(max_length=420)
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'


class Connection(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
