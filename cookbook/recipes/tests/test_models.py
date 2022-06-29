from django.test import TestCase
from django.db import models
import datetime
from ..models import Quantity,Unit,Time, Necessity, Ingredient, QuantityUnitIngredient, QuantityUnitNecessity, Kitchen, Recipe

class QuantityModelTestCase(TestCase):
    def setUp(self):
        self.quantity = Quantity(quantity=1)
    def test_quantity_consists_of_Quantity_and_integer(self):
        self.assertIsInstance(self.quantity,Quantity)
        self.assertIsInstance(isinstance(self.quantity.quantity,int),int)

class UnitModelTestCase(TestCase):
    def setUp(self):
        self.unit = Unit(unit="ml")
    def test_unit_consists_of_Unit_and_string(self):
        self.assertIsInstance(self.unit,Unit)
        self.assertTrue(isinstance(self.unit.unit,str), str)

class  TimeModelTestCase(TestCase):
    def setUp(self):
        self.time = Time(time=datetime.time(0,25,0))

    def test_time_consists_of_Time_and_time(self):
        self.assertIsInstance(self.time,Time)
        self.assertIsInstance(self.time.time,datetime.time)

class NecessityModelTestCase(TestCase):
    def setUp(self):
        self.necessity = Necessity(necessity_name="snijplank")
    def test_necessity_consists_of_Necessity_and_string(self):
        self.assertIsInstance(self.necessity,Necessity)
        self.assertIsInstance(self.necessity.necessity_name,str)

class IngredientModelTestCase(TestCase):
    def setUp(self):
        self.ingredient = Ingredient(ingredient_name="gehakt")
    def test_ingredient_consists_of_Ingredient_and_string(self):
        self.assertIsInstance(self.ingredient,Ingredient)
        self.assertIsInstance(self.ingredient.ingredient_name,str)

class QuantityUnitIngredientModelTestCase(TestCase):
    def setUp(self):
        self.quantity = Quantity(quantity=100)
        self.unit = Unit(unit="gram")
        self.ingredient = Ingredient(ingredient_name="gehakt")
        self.hunderd_gram_gehakt = QuantityUnitIngredient(ingredient=self.ingredient.pk,quantity=self.quantity.pk,unit=self.unit.pk)
    def test_hunderd_gram_gehakt_consists_of_QuantityUnitIngredient(self):
        self.assertIsInstance(self.hunderd_gram_gehakt,QuantityUnitIngredient)

class QuantityUnitNecessityModelTestCase(TestCase):
    def setUp(self):
        self.quantity = Quantity(quantity=1)
        self.unit = Unit(unit="stuk")
        self.necessity = Necessity(necessity_name="snijplank")
        self.one_stuk_snijplank = QuantityUnitNecessity(necessity=self.necessity.pk,quantity=self.quantity.pk,unit=self.unit.pk)
    def test_one_stuk_snijplank_consists_of_QuantityUnitNecessity(self):
        self.assertIsInstance(self.one_stuk_snijplank, QuantityUnitNecessity)

class KitchenModelTestCase(TestCase):
    def setUp(self):
        self.kitchen = Kitchen(name="Italiaans",description="De Italiaanse keuken is in vele landen bekend, en wordt wereldwijd geïmiteerd. Internationaal vindt men pizzeria's en in veel huishoudens worden er op de Italiaanse keuken gebaseerde pastagerechten gemaakt. Kaas en wijn spelen een grote rol. Het land kent dan ook vele kazen en wijnen met hun eigen regionale keurmerk.")

    def test_kitchen_consists_of_Kitchen_and_strings(self):
        self.assertIsInstance(self.kitchen,Kitchen)
        self.assertIsInstance(self.kitchen.name, str)
        self.assertIsInstance(self.kitchen.description,str)


class RecipeModelTestCase(TestCase):

    def setUp(self):
        self.quantity = Quantity(quantity=1)
        self.time = Time(time=datetime.time(0, 25, 0))
        self.time.save()
        self.necessity = Necessity(necessity_name="snijplank")
        self.ingredient = Ingredient(ingredient_name="gehakt")
        self.unit = Unit(unit="gram")
        self.hunderd_gram_gehakt = QuantityUnitIngredient(ingredient=self.ingredient.pk, quantity=self.quantity.pk,
                                                          unit=self.unit.pk)
        self.quantity_one = Quantity(quantity=1)
        self.unit_stuk = Unit(unit="stuk")
        self.necessity = Necessity(necessity_name="snijplank")
        self.one_stuk_snijplank = QuantityUnitNecessity(necessity=self.necessity.pk, quantity=self.quantity_one.pk,
                                                        unit=self.unit_stuk.pk)
        self.kitchen = Kitchen(name="Italiaans",
                               description="De Italiaanse keuken is in vele landen bekend, en wordt wereldwijd geïmiteerd. Internationaal vindt men pizzeria's en in veel huishoudens worden er op de Italiaanse keuken gebaseerde pastagerechten gemaakt. Kaas en wijn spelen een grote rol. Het land kent dan ook vele kazen en wijnen met hun eigen regionale keurmerk.")
        self.preparation = "De marinade van de vis heb je toch het volgende nodig: witvis, tikka massala en griekse yoghurt? En dan marineren en 20 minuten op de grillstand van de oven op 200 graden zetten? "
        self.recipe = Recipe(id=1,name="test",time=self.time,number_of_persons=4,kitchen=self.kitchen,preparation=self.preparation )
        self.recipe.ingredients.set([self.hunderd_gram_gehakt.pk])
        self.recipe.necessities.set([self.one_stuk_snijplank.pk])


    def test_recipe_consists_of_multiple_models(self):
        self.assertIsInstance(self.recipe,Recipe)
        self.assertIsInstance(self.recipe.name,str)
        self.assertIsInstance(self.recipe.time,Time)
        self.assertIsInstance(self.recipe.number_of_persons,int)
        self.assertIsInstance(self.recipe.kitchen,Kitchen)
        """ 
        self.assertIsInstance(self.recipe.ingredients,models.ManyToManyField)
       
        self.assertIsInstance(self.recipe.necessities, set<QuantityUnitNecessity>)
         """
        self.assertIsInstance(self.recipe.preparation,str)
