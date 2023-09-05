from django.shortcuts import render


def index(request):
    return render(
        request,
        'AppDesignPattern/pages/index.html'
    )
