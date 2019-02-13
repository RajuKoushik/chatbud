from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from .models import *


@login_required
def home(request):
    groups = Group.objects.all()
    return render(request, 'chatapi/home.html', {'groups': groups})


@login_required
def create_group(request):
    current_user = request.user

    if request.method == "POST":
        print(current_user)
        print(request.POST.get("group_name"))
        print(request.POST.get("group_description"))

        new_group = Group()
        new_group.admin = current_user
        new_group.title = request.POST.get("group_name")
        new_group.description = request.POST.get("group_description")
        new_group.save()

        connection = Connection()
        connection.group = new_group
        connection.user = current_user
        connection.save()

    return render(request, 'chatapi/create_group.html', {'current_user': current_user, })


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


# @login_required
# def send_message(request, group_id):
#
#     user = request.user
#     current_user = user
#
#     group_details = Group.objects.get(pk=group_id)
#     messages = Message.objects.filter(group=group_details)
#
#     user = User.objects.get(username=current_user.username)
#     connection = Connection.objects.filter(group=group_details)
#
#     if request.method == "POST":
#         import pdb;pdb.set_trace()
#         print(group_id)
#         print(request.POST.get("message"))
#         group = Group.objects.get(pk=group_id)
#         current_user = request.user
#         message_object = Message()
#         message_object.group = group
#         message_object.author = current_user
#         message_object.content = request.POST.get("message")
#         message_object.save()
#
#         # getting back
#
#
#
#     return render(request, 'chatapi/group_chat.html',
#                   {'messages': messages, 'group_details': group_details, 'user': user, 'connection': connection,
#                    'current_user': current_user})


@login_required
@csrf_exempt
def send_message(request, group_id):
    group_details = Group.objects.get(pk=group_id)
    messages = Message.objects.filter(group=group_details)
    current_user = request.user
    user = User.objects.get(username=current_user.username)
    connection = Connection.objects.filter(group=group_details)
    message_object = Message()
    print("hi")
    sucess = False
    print(group_id)
    print(request.POST.get("message"))
    group = Group.objects.get(pk=group_id)
    current_user = request.user

    message_object.group = group
    message_object.author = current_user
    message_object.content = request.POST.get("message")
    message_object.save()

    # getting back

    group_details = Group.objects.get(pk=group_id)
    messages = Message.objects.filter(group=group_details)

    user = User.objects.get(username=current_user.username)
    connection = Connection.objects.filter(group=group_details)
    success = True

    # return render(request, 'chatapi/group_chat.html',
    #               {'messages': messages, 'group_details': group_details, 'user': user, 'connection': connection,
    #                'current_user': current_user, 'date': str(message_object.created), 'is_success': success })

    data = {
        'is_success': success
    }

    return JsonResponse(data)
