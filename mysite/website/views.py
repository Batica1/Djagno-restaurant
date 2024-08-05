from django.shortcuts import render

from website.models import Orders
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})

@csrf_protect
def order(request):
    if request.method=="POST":
        if request.POST.get('name') and \
            request.POST.get('email') and \
            request.POST.get('food') and \
            request.POST.get('payment') or \
            request.POST.get('expectation'):
            
            orders = Orders()
            orders.name=request.POST.get('name')
            orders.email=request.POST.get('email')
            orders.food=request.POST.get('food')
            orders.payment=request.POST.get('payment')
            orders.expectation=request.POST.get('expectation')
            
            orders.save()
            return HttpResponseRedirect('/')
    else:
         return render(request, 'order.html', {})


def contact(request):
    return render(request, 'contact.html', {})
