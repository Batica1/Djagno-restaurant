from django.contrib import admin
from django.views.decorators.csrf import csrf_protect
# Register your models here.
from .models import Orders

admin.site.register(Orders)