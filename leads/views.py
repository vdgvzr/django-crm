from django.shortcuts import render


def home_page(request):

    template = "leads/home_page.html"
    context = {}

    return render(request, template, context)
