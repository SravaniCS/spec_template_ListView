from django.shortcuts import render

# Create your views here.
from app.models import *
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy


class SchoolList(ListView):
    model=School #it will retrive all the data from the specifed table
    context_object_name='schools' #this will take the objects and store them in the form of context under name 'schools' and send it to frontend
    #ordering='sname' #It displays the objects according to Alphabets, by default it displays in insertion order
    #queryset=School.objects.filter(id=3) # we can write the queryset to customize(not mandatory)
    #template_name='school_list.html' #not manadatory

class SchoolDetails(DetailView):
    model=School
    context_object_name='sclobject'



class SchoolCreate(CreateView):
    model=School
    fields='__all__'


class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'


class SchoolDelete(DeleteView):
    model=School
    context_object_name='schoolobj'
    success_url=reverse_lazy('SchoolList')
