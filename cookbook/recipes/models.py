from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from django.urls import reverse


class Quantity(models.Model):
    quantity = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return str(self.quantity)

class Unit(models.Model):
    unit = models.CharField(max_length=50)

    def __str__(self):
        return str(self.unit)

class Time(models.Model):
    time = models.TimeField(auto_now=False, auto_now_add=False,unique=True)

    def __str__(self):
        return str(self.time)

class Necessity(models.Model):
    necessity_name = models.CharField(max_length=250,unique=True)

    def __str__(self):
        return self.necessity_name


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=250,unique=True)

    def __str__(self):
        return  self.ingredient_name

class QuantityUnitIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient,on_delete=models.CASCADE)
    quantity = models.ForeignKey(Quantity,on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit,on_delete=models.CASCADE)

    def __str__(self):
      return "{quantity}  {unit} {ingredient}".format(ingredient=self.ingredient,quantity=self.quantity,unit=self.unit)


class QuantityUnitNecessity(models.Model):
    necessity = models.ForeignKey(Necessity,on_delete=models.CASCADE)
    quantity = models.ForeignKey(Quantity, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return "{quantity}  {unit}  {necessity}".format(necessity=self.necessity, quantity=self.quantity,
                                                        unit=self.unit)
class Kitchen(models.Model):
    name = models.CharField(max_length=250,unique=True)
    description = models.TextField(max_length=750)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=250,unique=True)
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    number_of_persons = models.IntegerField()
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(QuantityUnitIngredient)
    necessities = models.ManyToManyField(QuantityUnitNecessity)
    preparation = models.TextField(max_length=5000)

    def __str__(self):
        return self.name

    def get_all_objects(self):
        # can use the below method also
        queryset = self.__class__.objects.all()
        return queryset

    def get_absolute_url(self):
        return reverse("recipes.detail", kwargs={"id": self.id})