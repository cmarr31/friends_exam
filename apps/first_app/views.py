# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User, Friend

from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'first_app/index.html')

def register(request):
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['id'] = result.id
    messages.success(request, "Successfully registered!")
    return redirect('/friends')

def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['id'] = result.id
    messages.success(request, "Successfully logged in!")
    return redirect('/friends')

def logout(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')

def friends(request):
    current = User.objects.get(id=request.session['id'])
    try:
        users = User.objects.all()
        people = []
        for each in users:
            if (each.id != request.session['id']):
                people.append(each)
    except KeyError:
        users = None

    try:
        friends = Friend.objects.filter(added_user=current)
        users_friends = []
        for each_friend in friends:
            users_friends.append(each_friend.main_user)
        other_users = []
        for each in people:
            if (each not in users_friends):
                other_users.append(each)
    except KeyError:
        friends = None

    context = {
        'current' : current,
        'users' : other_users,
        'friends' : users_friends,
    }
    return render(request, 'first_app/success.html', context)

def show(request, id):
    user_profile = User.objects.get(id=id)
    context = {
        'user': user_profile
    }
    return render(request, 'first_app/show.html', context)

def add_friend(request, id):
    User.userManager.addFriend(request.session['id'], id)
    return redirect('/friends')

def delete_friend(request, id):
    User.userManager.deleteFriend(request.session['id'], id)
    return redirect('/friends')

#def success(request):
#    try:
#        request.session['user_id']
#    except KeyError:
#        return redirect('/')
#    context = {
#        'user': User.objects.get(id=request.session['user_id'])
#    }
#    return render(request, 'first_app/success.html', context)

#def show(request, user_id):
#    user = User.objects.get(id=user_id)
#    return render(request, 'first_app/show.html', context)