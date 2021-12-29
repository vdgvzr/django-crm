from django.shortcuts import reverse
from .models import Lead
from .forms import LeadModelForm
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


class LandingPageView(TemplateView):
    template_name = "landing.html"


''' def landing_page(request):
    template = "landing.html"
    return render(request, template) '''


class LeadListView(ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


''' def lead_list(request):
    template = "leads/lead_list.html"
    leads = Lead.objects.all()
    context = {
        "leads": leads,
    }

    return render(request, template, context) '''


class LeadDetailView(DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


''' def lead_detail(request, pk):
    template = "leads/lead_detail.html"
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead,
    }
    return render(request, template, context) '''


class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")


''' def lead_create(request):
    template = "leads/lead_create.html"
    form = LeadModelForm()

    if request.method == 'POST':
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("/leads")

    context = {
        "form": form
    }
    return render(request, template, context) '''


class LeadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")


''' def lead_update(request, pk):
    template = "leads/lead_update.html"
    lead = Lead.objects.get(pk=pk)
    form = LeadModelForm(instance=lead)

    if request.method == 'POST':
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()

            return redirect("/leads")

    context = {
        "lead": lead,
        "form": form
    }
    return render(request, template, context) '''


class LeadDeleteView(DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")


''' def lead_delete(request, pk):
    lead = Lead.objects.get(pk=pk)
    lead.delete()
    return redirect("/leads") '''
















''' def lead_update(request, pk):
    template = "leads/lead_update.html"
    lead = Lead.objects.get(pk=pk)
    form = LeadForm()
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            lead.first_name = first_name
            lead.last_name = last_name
            lead.age = age

            lead.save()

            return redirect("/leads")
    context = {
        "lead": lead,
        "form": form
    }
    return render(request, template, context) '''


''' def lead_create(request):
    form = LeadForm()
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.first()

            Lead.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                agent=agent
            )

            return redirect("/leads")

    template= "leads/lead_create.html"
    context = {
        "form": form
    }
    return render(request, template, context) '''