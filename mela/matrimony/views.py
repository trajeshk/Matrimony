#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView

from matrimony.models import Application

class ApplicationList(ListView):
    model = Application

class ApplicationCreate(CreateView):
    model = Application
    success_url = reverse_lazy('application_list')
    fields = ['name', 'date_of_birth', 'time', 'place', 'origin', 'gothram', 'family_name', 'natchathram', 'padam', 'rasi', 'height', 'colour', 'blood_group', 'mother_f_name', 'education', 'employment_details', 'office_address', 'email_address', 'salary', 'father_name', 'mother_name', 'applicant_is', 'brief_information', 'contact_address', 'phone', 'mobile', 'having_house', 'languages_known', 'marital_status', 'education_bride', 'origin_place', 'living_in', 'working_in', 'doing_business', 'height_shld_be', 'bride_for_job', 'bride_forced', 'horoscope', 'need' ]

class ApplicationUpdate(UpdateView):
    model = Application
    success_url = reverse_lazy('application_list')
    fields = ['name', 'date_of_birth', 'time', 'place', 'origin', 'gothram', 'family_name', 'natchathram', 'padam', 'rasi', 'height', 'colour', 'blood_group', 'mother_f_name', 'education', 'employment_details', 'office_address', 'email_address', 'salary', 'father_name', 'mother_name', 'applicant_is', 'brief_information', 'contact_address', 'phone', 'mobile', 'having_house', 'languages_known', 'marital_status', 'education_bride', 'origin_place', 'living_in', 'working_in', 'doing_business', 'height_shld_be', 'bride_for_job', 'bride_forced', 'horoscope', 'need' ]

class ApplicationDelete(DeleteView):
    model = Application
    success_url = reverse_lazy('application_list')

class ApplicationDetail(DetailView):
    model = Application
    success_url = reverse_lazy('application_list')

