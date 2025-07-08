from django.db import models

# Create your models here.

class Order(models.Model):
    PAYMENT_CHOICES = [
        ('easypaisa', 'EasyPaisa'),
        ('jazzcash', 'JazzCash'),
        ('cod', 'Cash on Delivery'),
    ]
    TIME_CHOICES = [
        ('morning', 'Morning'),
        ('evening', 'Evening'),
    ]

    method = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    delivery_time = models.CharField(max_length=10, choices=TIME_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone} - {self.method}"

from django.db import models
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name}"


