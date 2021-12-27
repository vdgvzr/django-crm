from django.shortcuts import render
from .models import Lead
from .forms import LeadForm


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
    form = LeadForm()
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']


    template= "leads/lead_create.html"
    context = {
        "form": form
    }
    return render(request, template, context)
