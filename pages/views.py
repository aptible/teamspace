from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt

from . import models


@csrf_exempt
@login_required
def add(request, username=None):
    if username is None:
        return HttpResponseNotFound()

    user = get_object_or_404(User, username=username)
    page = get_object_or_404(models.Page, user=user)

    context = {
        'user': user,
    }

    if request.POST:
        content = request.POST.get('content')
        models.Post.objects.create(page=page, user=request.user, content=content)
        return redirect('/pages/view/{}'.format(username))

    return render(request, 'add.html', context=context)


@login_required
def css(request, username=None):
    if username is None:
        return HttpResponseNotFound()

    user = get_object_or_404(User, username=username)
    page = get_object_or_404(models.Page, user=user)

    response = render(request, 'static.css', context={'css': page.css})
    response['Content-Type'] = 'text/css'
    return response


@csrf_exempt
@login_required
def edit(request):
    page = get_object_or_404(models.Page, user=request.user)
    if request.POST:
        if request.FILES:
            page.profile_pic = request.FILES.get('profile_pic').file.read()
        page.css = request.POST.get('css')
        page.js = request.POST.get('js')
        page.about = request.POST.get('about')
        page.save()

    context = {
        'about': page.about,
        'css': page.css,
        'js': page.js,
    }
    return render(request, 'edit.html', context=context)


@login_required
def index(request):
    user = request.user

    context = {
        'current_user': user,
        'posts': models.Post.objects.filter(parent=None)[0:10],
        'users': User.objects.all()
    }
    return render(request, 'index.html', context=context)


@login_required
def js(request, username=None):
    if username is None:
        return HttpResponseNotFound()

    user = get_object_or_404(User, username=username)
    page = get_object_or_404(models.Page, user=user)

    response = render(request, 'static.js', context={'js': page.js})
    response['Content-Type'] = 'text/javascript'
    return response


@login_required
def pic(request, username=None):
    if username is None:
        return HttpResponseNotFound()

    user = get_object_or_404(User, username=username)
    page = get_object_or_404(models.Page, user=user)

    response = HttpResponse()
    response['Content-Type'] = 'image/png'
    response.write(page.profile_pic)
    return response


@csrf_exempt
@login_required
def reply(request, post_id=None):
    if post_id is None:
        return HttpResponseNotFound()

    post = get_object_or_404(models.Post, id=post_id)
    if request.POST:
        content = request.POST.get('content')
        models.Post.objects.create(parent=post, page=post.page, user=request.user, content=content)
        return redirect('/pages/view/{}'.format(post.page.user.username))

    return render(request, 'reply.html', context={'post': post})


@csrf_exempt
@login_required
def search(request):
    if not request.POST:
        return render(request, 'search.html')

    date = request.POST.get('date')
    term = request.POST.get('term')
    username = request.POST.get('username')
    user = User.objects.filter(username=username).first()

    posts = models.Post.objects.all()

    if date:
        start = '{} 00:00'.format(date)
        stop = '{} 23:59'.format(date)
        posts = posts.filter(created_at__range=[start, stop])

    if term:
        posts = posts.filter(content__contains=term)

    if user and username:
        posts = posts.filter(user=user)
    elif username:
        # This ensures we return no results when
        # searching for a bad user.
        posts = posts.filter(user_id=0)

    context = {
        'date': date,
        'posts': posts,
        'term': term,
        'username': username,
    }
    return render(request, 'search.html', context=context)


@login_required
def view(request, username=None):
    if username is None:
        return HttpResponseNotFound()

    user = get_object_or_404(User, username=username)
    page = get_object_or_404(models.Page, user=user)
    posts = models.Post.objects.filter(
        page=page, parent=None
    ).order_by('-created_at')[0:10]

    context = {
        'page': page,
        'posts': posts,
        'user': user,
    }
    return render(request, 'view.html', context=context)
