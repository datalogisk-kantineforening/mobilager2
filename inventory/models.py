from django.db import models
from django.contrib.auth.models import User


class Vendor(models.Model):
    name = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    categories = tuple(enumerate(('Sellable',
                                  'Refundable')))
    default_cat = categories[0][0]

    name = models.CharField(max_length=255)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    discontinued = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    category = models.IntegerField(choices=categories,
                                   default=default_cat)

    def __str__(self):
        return str(self.name)


class EventType(models.Model):
    tag = models.CharField(max_length=20)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class Event(models.Model):
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    logged_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.description)

    class Meta:
        ordering = ["date", "time"]


class EventByUser(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Change(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    delta = models.IntegerField()
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.product)

    def changed(self):
        return self.delta != 0
