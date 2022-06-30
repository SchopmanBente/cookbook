from pprint import pprint

from django.test import TestCase
from model_bakery import baker
import datetime
from ..models import Quantity, Unit, Time, Necessity, Ingredient, QuantityUnitIngredient, QuantityUnitNecessity,  Kitchen, Recipe


class QuantityModelTestCase(TestCase):
    def setUp(self):
        self.quantity = baker.make('recipes.Quantity')

    def test_quantity_consists_of_Quantity_and_integer(self):
        self.assertIsInstance(self.quantity, Quantity)
        self.assertIsInstance(isinstance(self.quantity.quantity, int), int)


class UnitModelTestCase(TestCase):
    def setUp(self):
        self.unit = baker.make('recipes.Unit')

    def test_unit_consists_of_Unit_and_string(self):
        self.assertIsInstance(self.unit, Unit)
        self.assertTrue(isinstance(self.unit.unit, str), str)


class TimeModelTestCase(TestCase):
    def setUp(self):
        self.time = baker.make('recipes.Time')

    def test_time_consists_of_Time_and_time(self):
        self.assertIsInstance(self.time, Time)
        self.assertIsInstance(self.time.hours, int)
        self.assertIsInstance(self.time.minutes, int)


class NecessityModelTestCase(TestCase):
    def setUp(self):
        self.necessity = baker.make('recipes.Necessity')

    def test_necessity_consists_of_Necessity_and_string(self):
        self.assertIsInstance(self.necessity, Necessity)
        self.assertIsInstance(self.necessity.necessity_name, str)


class IngredientModelTestCase(TestCase):
    def setUp(self):
        self.ingredient = baker.make('recipes.Ingredient')

    def test_ingredient_consists_of_Ingredient_and_string(self):
        self.assertIsInstance(self.ingredient, Ingredient)
        self.assertIsInstance(self.ingredient.ingredient_name, str)


class QuantityUnitIngredientModelTestCase(TestCase):
    def setUp(self):
        self.hunderd_gram_gehakt = baker.make('recipes.QuantityUnitIngredient', make_m2m=True)

    def test_hunderd_gram_gehakt_consists_of_QuantityUnitIngredient(self):
        self.assertIsInstance(self.hunderd_gram_gehakt, QuantityUnitIngredient)


class QuantityUnitNecessityModelTestCase(TestCase):
    def setUp(self):
        self.one_stuk_snijplank = baker.make('recipes.QuantityUnitNecessity', make_m2m=True)

    def test_one_stuk_snijplank_consists_of_QuantityUnitNecessity(self):
        self.assertIsInstance(self.one_stuk_snijplank, QuantityUnitNecessity)


class KitchenModelTestCase(TestCase):
    def setUp(self):
        self.kitchen = baker.make('recipes.Kitchen')
    def test_kitchen_consists_of_Kitchen_and_strings(self):
        self.assertIsInstance(self.kitchen, Kitchen)
        self.assertIsInstance(self.kitchen.name, str)
        self.assertIsInstance(self.kitchen.description, str)


class RecipeModelTestCase(TestCase):
    @classmethod
    def setUp(self):
        self.recipe =  baker.make('recipes.Recipe')
        self.recipe.save()
        self.ingredient1 = baker.make('recipes.QuantityUnitIngredient', make_m2m=True)
        self.ingredient1.save()
        pprint(self.ingredient1.__dict__)
        self.recipe.ingredients.add(self.ingredient1)
        self.necessity1 = baker.make('recipes.QuantityUnitNecessity', make_m2m=True)
        self.necessity1.save()
        self.recipe.necessities.add(self.necessity1)
        pprint(self.necessity1.__dict__)
        pprint(self.recipe.__dict__)

    def test_recipe_consists_of_multiple_models(self):
        self.assertIsInstance(self.recipe, Recipe)
        self.assertIsInstance(self.recipe.name, str)
        self.assertIsInstance(self.recipe.time, Time)
        self.assertIsInstance(self.recipe.number_of_persons, int)
        self.assertIsInstance(self.recipe.kitchen, Kitchen)
        self.assertIsInstance(self.recipe.preparation, str)

    def test_recipe_has_ingredients(self):
        self.assertEqual(self.recipe.ingredients.count(), 1)

    def test_recipe_has_necessities(self):
        self.assertEqual(self.recipe.necessities.count(),1)


class AddQuantityUnitIngredient(TestCase):
    def setUp(self):
        self.quantity = Quantity.objects.create(quantity=100)
        self.unit = Unit.objects.create(unit="gram")
        self.ingredient = Ingredient.objects.create(ingredient_name="komkommer")
        self.hunderd_gram_komkommer = QuantityUnitIngredient(ingredient=self.ingredient,quantity=self.quantity, unit=self.unit )

    def test_check_types(self):
        self.assertIsInstance(self.quantity,Quantity)
        self.assertIsInstance(self.unit,Unit)
        self.assertIsInstance(self.ingredient,Ingredient)
        self.assertIsInstance(self.hunderd_gram_komkommer,QuantityUnitIngredient)

class  AddQuantityUnitIngredientToRecipe(TestCase):
    def setUp(self):
        self.recipe = baker.make('recipes.Recipe')
        self.recipe.save()
        self.ingredient1 = baker.make('recipes.QuantityUnitIngredient', make_m2m=True)
        self.ingredient1.save()
        pprint(self.ingredient1.__dict__)
        self.recipe.ingredients.add(self.ingredient1)

    def test_recipe_has_ingredients(self):
        self.assertEqual(self.recipe.ingredients.count(), 1)