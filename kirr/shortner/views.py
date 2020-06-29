from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.

#this is function based view
def kirr_redirect_view(request,*args,**kwargs):
    return HttpResponse("Hello")

#this is class based view
class KirrRedirectView(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse('Hello again')
