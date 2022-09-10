from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import URLPattern, URLResolver
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from url_status_checker.forms import RegisterForm

urlconf = __import__(settings.ROOT_URLCONF, {}, {}, [''])


def list_urls(lis, acc=None):
    if acc is None:
        acc = []
    if not lis:
        return
    l = lis[0]
    if isinstance(l, URLPattern):
        yield acc + [str(l.pattern)]
    elif isinstance(l, URLResolver):
        yield from list_urls(l.url_patterns, acc + [str(l.pattern)])
    yield from list_urls(lis[1:], acc)


def index(request):
    if request.user.is_authenticated:
        result = []
        for p in list_urls(urlconf.urlpatterns):
            result.append(p)
        raw_url = []
        for i in result:
            raw_url.append("".join(i))

        return render(request, "url_status_checker/index.html", {"urls": raw_url})

    return redirect("login")


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.errors:
            return render(request, "url_status_checker/index.html", {"error": form.errors})
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            user.save()
            return redirect("login")

    form = RegisterForm()
    return render(request, "url_status_checker/register.html", {"form": form})
