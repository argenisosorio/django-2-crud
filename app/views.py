# -*- coding: utf-8 -*-
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from app.models import Person
from app.forms import PersonForm


class Index(TemplateView):
    template_name = "app/index.html"


class List(ListView):
    model = Person


class Create(CreateView):
    model = Person
    form_class = PersonForm
    #fields = ['first_name', 'last_name']
    success_url = reverse_lazy('list')


class Update(UpdateView):
    model = Person
    form_class = PersonForm
    #fields = ['first_name', 'last_name']
    success_url = reverse_lazy('list')


class Delete(DeleteView):
    model = Person
    success_url = reverse_lazy('list')
