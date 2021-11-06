from django.shortcuts import render
from .models import Lead


def lead_list(request):
    template = "leads/lead_list.html"
    leads = Lead.objects.all()
    context = {
        "leads": leads,
    }

    return render(request, template, context)


def lead_detail(request, pk):
    template = "leads/lead_detail.html"
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead,
    }
    return render(request, template, context)


def lead_create(request):
    template= "leads/lead_create.html"
    context = {}
    return render(request, template, context)
