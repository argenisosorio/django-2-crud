# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from app.models import Person
from django.template import RequestContext


class Index(TemplateView):
    template_name = "app/index.html"


class List(ListView):
    model = Person


class Create(CreateView):
    model = Person
    fields = ['first_name', 'last_name']
    success_url = reverse_lazy('list')


class Update(UpdateView):
    model = Person
    fields = ['first_name', 'last_name']
    success_url = reverse_lazy('list')


class Delete(DeleteView):
    model = Person
    success_url = reverse_lazy('list')
