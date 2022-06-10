from audioop import reverse
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Snack
from django.views.generic import (

ListView,
DetailView,
CreateView,
UpdateView,
DeleteView,
TemplateView

) 
# Create your views here.

class SnackListView (ListView):
    """
    Create SnackListView that extends appropriate generic view
associated url path is an empty string
    """
    template_name="snack_list.html"
    model=Snack


 


class SnackDetailView(DetailView):
    """
    Create SnackDetailView that extends appropriate generic view
associated url path is <int:pk>/
    """
    template_name="snack_detail.html"
    model=Snack


class SnackCreateView (CreateView):
    """
    Create SnackCreateView that extends appropriate generic view
associated url path is create/
    """

    template_name="snack_create.html"
    model=Snack
    fields= ["title" ,"description","purchaser"]


class SnackUpdateView (UpdateView):
    """
    Create SnackUpdateView that extends appropriate generic view
associated url path is <int:pk>/update/
    """
    template_name="snack_update.html"
    model=Snack
    fields= ["title" ,"description","purchaser"]



class SnackDeleteView (DeleteView):
    """
    Create SnackDeleteView that extends appropriate generic view
associated url path is <int:pk>/delete/

    """
    template_name="snack_delete.html"
    model=Snack
    success_url= reverse_lazy('snack_list')
