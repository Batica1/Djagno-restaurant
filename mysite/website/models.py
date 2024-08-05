from django.db import models
from django.views.decorators.csrf import csrf_protect
class Orders(models.Model):

    FOOD = (
			('Italian', 'Italian'),
			('Mexican', 'Mexican'),
			('Japanese', 'Japanese'),
			('Greek', 'Greek'),
            ('German', 'German'),
			)

    PAYMENT = (
        ('cash', 'Cash'),
        ('card', 'Card'),
        )

    id=models.IntegerField(primary_key=True)

    name=models.CharField(max_length=100)

    email=models.CharField(max_length=100)

    food=models.CharField(max_length=200, null=True, choices=FOOD)

    payment=models.CharField(max_length=200, null=True, choices=PAYMENT)
    
    expectation=models.CharField(max_length=100)
   
    created_at = models.DateTimeField(auto_now_add=True) 
    
    class Meta:
        db_table="orders"

    
      