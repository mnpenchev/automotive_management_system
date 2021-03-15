from django.db import models


class CarOwner(models.Model):
    CHOICES = [('Factory', 'Factory'), ('Dealership', 'Dealership'), ('Client', 'Client'), ]
    owner_type = models.CharField(max_length=11, choices=CHOICES)

    def __str__(self):
        return self.owner_type


class Factory(CarOwner):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Factories"

    def __str__(self):
        return self.name


class Dealership(CarOwner):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    factory = models.ManyToManyField(Factory)

    def __str__(self):
        return self.name


class Client(CarOwner):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dealerships = models.ForeignKey(Dealership, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Car(models.Model):
    MODEL_CHOICES = [('SEDAN', 'Sedan'), ('COUPE', 'Coupe'), ('VAN', 'Van'), ('SUV', 'Suv'), ]
    TYPE_CHOICES = [('S', 'S'), ('L', 'L'), ('M', 'M'), ]
    COLOR_CHOICES = [('White', 'White'), ('Black', 'Black'), ('Red', 'Red'), ('Blue', 'Blue'), ]

    model = models.CharField(max_length=255, choices=MODEL_CHOICES, default='sedan')
    type = models.CharField(max_length=255, choices=TYPE_CHOICES, default='M')
    color = models.CharField(max_length=255, choices=COLOR_CHOICES, default='white')

    produced = models.DateField(auto_now=False)
    vin = models.CharField(max_length=25, blank=False)
    car_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.model}, {self.type}, {self.color}, {self.vin}, {self.car_owner}'
