from django.conf import settings
from django.contrib import auth
from django.shortcuts import redirect, render
from django.utils.encoding import iri_to_uri
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.csrf import csrf_exempt


def base_css(request):
    response = render(request, 'base.css')
    response['Content-Type'] = 'text/css'
    return response


@csrf_exempt
def login(request):
    next = request.GET.get('next') or request.POST.get('next') or '/'
    next = iri_to_uri(next)
    if not url_has_allowed_host_and_scheme(next, settings.ALLOWED_HOSTS):
        next = '/'

    if request.user.is_authenticated:
        return redirect(next)

    context = {
        'next': next,
    }

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = None

    if username and password:
        user = auth.authenticate(request, username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect(next)

    if username and password and user is None:
        context['error'] = 'Invalid username or password'

    return render(request, 'login.html', context=context)


def logout(request):
    auth.logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)
