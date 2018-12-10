from django.shortcuts import render
from django.views import generic
from .models import Person
class IndexView(generic.ListView):
    template_name = 'myapp/index.html'
    def get_queryset(self):
        return Person.objects.all()