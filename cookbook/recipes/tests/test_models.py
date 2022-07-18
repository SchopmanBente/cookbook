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

    def test_quantity_string_is_string_of_quantity(self):
        self.assertIs(type(self.quantity.__str__()), str)

    """ 
    def test_quantity_string_is_the_same(self):
        self.assertIs(self.quantity.__str__(), str(self.quantity.quantity))
    """
class UnitModelTestCase(TestCase):
    def setUp(self):
        self.unit = baker.make('recipes.Unit')

    def test_unit_consists_of_Unit_and_string(self):
        self.assertIsInstance(self.unit, Unit)
        self.assertTrue(isinstance(self.unit.unit, str), str)

    def test_unit_prints_string(self):
        self.assertIsInstance(self.unit.unit, str)
        self.assertTrue(id(self.unit.__str__()),id(self.unit.unit))


class TimeModelTestCase(TestCase):
    def setUp(self):
        self.time = baker.make('recipes.Time')

    def test_time_consists_of_Time_and_time(self):
        self.assertIsInstance(self.time, Time)
        self.assertIsInstance(self.time.hours, int)
        self.assertIsInstance(self.time.minutes, int)

    def test_time_prints_string(self):
        self.assertTrue(id(self.time.__str__()), id("Uren:{hours} Minuten: {minutes}".format(hours=str(self.time.hours), minutes=str(self.time.minutes))))

class NecessityModelTestCase(TestCase):
    def setUp(self):
        self.necessity = baker.make('recipes.Necessity')

    def test_necessity_consists_of_Necessity_and_string(self):
        self.assertIsInstance(self.necessity, Necessity)
        self.assertIsInstance(self.necessity.necessity_name, str)

    def test_necessity_prints_string(self):
        self.assertTrue(self.necessity.__str__(), self.necessity.necessity_name)


class IngredientModelTestCase(TestCase):
    def setUp(self):
        self.ingredient = baker.make('recipes.Ingredient')

    def test_ingredient_consists_of_Ingredient_and_string(self):
        self.assertIsInstance(self.ingredient, Ingredient)
        self.assertIsInstance(self.ingredient.ingredient_name, str)

    def test_ingredient_prints_string(self):
        self.assertIs(self.ingredient.__str__(), self.ingredient.ingredient_name)

class QuantityUnitIngredientModelTestCase(TestCase):
    def setUp(self):
        self.hunderd_gram_gehakt = baker.make('recipes.QuantityUnitIngredient', make_m2m=True)

    def test_hunderd_gram_gehakt_consists_of_QuantityUnitIngredient(self):
        self.assertIsInstance(self.hunderd_gram_gehakt, QuantityUnitIngredient)

    def test_QuantityUnitIngredient_prints_string(self):
        self.assertTrue(id(self.hunderd_gram_gehakt.__str__()), id("{quantity}  {unit} {ingredient}".format(ingredient=self.hunderd_gram_gehakt.ingredient,quantity=self.hunderd_gram_gehakt.quantity,unit=self.hunderd_gram_gehakt.unit)))


class QuantityUnitNecessityModelTestCase(TestCase):
    def setUp(self):
        self.one_stuk_snijplank = baker.make('recipes.QuantityUnitNecessity', make_m2m=True)

    def test_one_stuk_snijplank_consists_of_QuantityUnitNecessity(self):
        self.assertIsInstance(self.one_stuk_snijplank, QuantityUnitNecessity)

    def test_QuantityUnitNecessity_prints_the_same_string(self):
        self.assertTrue(id(self.one_stuk_snijplank.__str__()), id("{quantity}  {unit}  {necessity}".format(necessity=self.one_stuk_snijplank.necessity, quantity=self.one_stuk_snijplank.quantity,
                                                        unit=self.one_stuk_snijplank.unit)))
class KitchenModelTestCase(TestCase):
    def setUp(self):
        self.kitchen = baker.make('recipes.Kitchen')
    def test_kitchen_consists_of_Kitchen_and_strings(self):
        self.assertIsInstance(self.kitchen, Kitchen)
        self.assertIsInstance(self.kitchen.name, str)
        self.assertIsInstance(self.kitchen.description, str)

    def test_kitchen_prints_the_same_string(self):
        self.assertTrue(id(self.kitchen.__str__()), id(self.kitchen.name))


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

    def test_recipe_prints_the_same_string(self):
        self.assertTrue(id(self.recipe.__str__()), id(self.recipe.name))

