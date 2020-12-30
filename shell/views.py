from django.http import HttpResponse


def index(request):
    return HttpResponse("This is main page of multishell")
