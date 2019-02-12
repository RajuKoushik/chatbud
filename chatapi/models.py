import uuid

from django.contrib.auth.models import User
from django.db import models
from django.db.models import UUIDField


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(default=0)
    join_date = models.DateTimeField('Join published', default='2011-11-11 11:11')

    def __str__(self):
        return self.user.first_name


class Message(models.Model):
    message_id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    content = models.TextField(max_length=420)
    author = models.ForeignKey(
        User, related_name='author', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'


class Group(models.Model):
    group_id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    description = models.TextField(max_length=420)
    admin = models.ForeignKey(
        User, related_name='admin', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'


class Connection(models.Model):
    connection_id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
