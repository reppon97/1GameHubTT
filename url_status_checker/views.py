from django.shortcuts import render


def index(request):
    return render(request, "url_status_checker/index.html")
