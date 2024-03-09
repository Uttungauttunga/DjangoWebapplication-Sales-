# models.py
from django.db import models


class Sale(models.Model):
    date = models.DateField()
    book_name = models.CharField(max_length=100, default='Unknown')
    number_of_books = models.IntegerField(default=0)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
