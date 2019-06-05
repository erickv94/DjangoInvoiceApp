from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

# Create your views here.
class HomeText(generic.View):
    def get(self,request,*args,**kwargs):
        return HttpResponse('Hello')

class Home(generic.TemplateView):
    template_name='base/base.html'
    
