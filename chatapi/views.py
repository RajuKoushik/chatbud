from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render

# Create your views here.
from .models import *


@login_required
def home(request):
    groups = Group.objects.all()
    return render(request, 'chatapi/home.html', {'groups': groups})


@login_required
def group_chat(request, group_id):
    group_details = Group.objects.get(pk=group_id)
    messages = Message.objects.filter(group=group_details)
    current_user = request.user

    print(current_user)

    user = User.objects.get(username=current_user.username)
    connection = Connection.objects.filter(group=group_details)

    try:
        group = Group.objects.get(pk=group_id)
    except Group.DoesNotExist:
        raise Http404("Group does not exist")

    return render(request, 'chatapi/group_chat.html',
                  {'messages': messages, 'group_details': group_details, 'user': user, 'connection': connection,
                   'current_user': current_user})


@login_required
def send_message(request, group_id):
    if request.method == "POST":
        print(group_id)
        print(request.POST.get("message"))
        group = Group.objects.get(pk=group_id)
        current_user = request.user
        message_object = Message()
        message_object.group = group
        message_object.author = current_user
        message_object.content = request.POST.get("message")
        message_object.save()

        # getting back

        group_details = Group.objects.get(pk=group_id)
        messages = Message.objects.filter(group=group_details)

        user = User.objects.get(username=current_user.username)
        connection = Connection.objects.filter(group=group_details)

    return render(request, 'chatapi/group_chat.html',
                  {'messages': messages, 'group_details': group_details, 'user': user, 'connection': connection,
                   'current_user': current_user})
