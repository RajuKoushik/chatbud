# Register your models here.

from django.contrib import admin

from .models import UserInfo, Message, Group, Connection

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Message)
admin.site.register(Group)
admin.site.register(Connection)
