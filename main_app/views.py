from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Patient

# Create your views here.

def home (request):
    return HttpResponse ('working so far')

def about (request):
    # return HttpResponse('<h1> This is the About page </h1>')
    return render(request, 'about.html')

def patients_index(request):
    patients = Patient.objects.all()
    return render(request, 'patients/index.html', {
        'patients': patients,
    })

from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.urls import reverse
from django.utils.safestring import mark_safe
import calendar

from cal.models import *
from cal.utils import Calendar
from cal.forms import EventForm

class CalendarView(ListView):
    model = Event 
    template_name = 'cal/calendar.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # d = get_date(self.request.GET.get('day', None))
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month,)
            
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
    
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context
    

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day = days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def patient_history(request, patient_id, event_id = None):
    patient = Patient.objects.get(id=patient_id)
    
    # instance = Event()
    # if event_id:
    #     instance = get_object_or_404(Event, pk=event_id)
    # else:
    #     instance = Event()
        
    # form = EventForm(request.POST or None, instance=instance)
    # if request.POST and form.is_valid():
    #     form.save()
    #     return HttpResponseRedirect(reverse('cal:calendar'))
    return render(request, 'patients/history.html', {
        'patient': patient, 
    })
    
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Patient, Service

class PatientCreate(CreateView):
    model = Patient
    fields = ['patient_name', 'patient_lastname', 'patient_species', 'patient_age', 'patient_gender', 'patient_weight', 'color' ]
    success_url = '/patients/'

class PatientUpdate(UpdateView):
    model = Patient
    fields = '__all__'

class PatientDelete(DeleteView):
    model = Patient
    success_url = '/patients/'

class ServiceList(ListView):
    model = Service

class ServiceCreate(CreateView):
    model = Service
    fields = '__all__'
