# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.db.models import F
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from item_inventory.models import Container, Item

# Create your views here.
class ContainerList(ListView):
    model = Container
    context_object_name = 'containers'
    template_name = 'containers/index.html'

class ContainerDetail(DetailView):
    model = Container
    template_name = 'containers/show.html'

class ContainerCreate(CreateView):
    model = Container
    fields = ['name']
    template_name = 'containers/form.html'
    success_url = reverse_lazy('item_inventory:index')

class ContainerUpdate(UpdateView):
    model = Container
    fields = ['name']
    template_name = 'containers/form.html'
    success_url = reverse_lazy('item_inventory:index')

class ContainerDelete(DeleteView):
    model = Item
    template_name = 'containers/confirm_delete.html'
    success_url = reverse_lazy('item_inventory:index')

class ItemList(ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'items/index.html'

class ItemDetail(DetailView):
    model = Item
    template_name = 'items/show.html'

class ItemCreate(CreateView):
    model = Item
    fields = ['name', 'quantity', 'container']
    template_name = 'items/form.html'
    success_url = reverse_lazy('item_inventory:items_index')

class ItemUpdate(UpdateView):
    model = Item
    fields = ['name', 'quantity', 'container']
    template_name = 'items/form.html'
    success_url = reverse_lazy('item_inventory:items_index')

class ItemDelete(DeleteView):
    model = Item
    template_name = 'items/confirm_delete.html'
    success_url = reverse_lazy('item_inventory:items_index')
