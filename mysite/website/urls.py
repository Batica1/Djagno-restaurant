
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_protect
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('order', views.order, name='order'),
    path('contact', views.contact, name='contact'),
]
