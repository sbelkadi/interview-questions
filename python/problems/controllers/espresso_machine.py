from typing import List
from .espresso_drink import EspressoDrink
import json
import numpy as np

class EspressoMachine:
    def __init__(self, drink_list: dict = None):
        if drink_list is None:
            drink_list = {}
        self._drink_list = drink_list

    # Fill in the function get_drink_params in espresso_machine.py which takes 
    # drink_name as a parameter and returns the following outputs for each drink:
    #   1. coffee (in grams)
    #   2. water (in mL)
    #   3. milk (in mL)
    def get_drink_params(self, drink_name: str) -> List[float]:
        if drink_name not in self._drink_list:
            raise Exception(f"{drink_name} is not in known list of drinks.")

        drink = self._drink_list[drink_name]
        
        # these are prepended with _ but are not private
        coffee_grams = drink._coffee
        water_mL = drink._water
        milk_mL = drink._milk

        return [coffee_grams, water_mL, milk_mL]

    # Fill in the add_drink_to_menu function which checks if a drink recipe is known and, if not, 
    # adds the drink to the list of known recipes.
    def add_drink_to_menu(self, drink_name: str):
        # check if drink is already known
        if drink_name in self._drink_list:
            print(f"{drink_name} is already known.")
        
        # read in all recipes from drinks list, and check to make sure drink is there
        with open('./data/drinks.json', 'r') as drink_file: 
            coffee_recipes = json.loads(drink_file.read())
        
        if drink_name not in coffee_recipes:
            raise Exception(f"{drink_name} could not be found in recipe list.")
        
        drink_recipe = coffee_recipes[drink_name]
        
        # check if the drink is an espresso drink, or other type of drink in list
        if drink_recipe.get('espresso_ratio'):
            milk_mL = self.calculate_mL_of_milk_drink(drink_recipe)
            coffee_grams = self.calculate_grams_of_coffee_drink(drink_recipe)
            water_mL = self.calculate_mL_of_water_drink(drink_recipe)
            order_size = drink_recipe['mL']
        else:
            milk_mL = self.calculate_mL_of_milk_other(drink_recipe)
            coffee_grams = self.calculate_grams_of_coffee_other(drink_recipe)
            water_mL = self.calculate_mL_of_water_other(drink_recipe)
            order_size = drink_recipe['mL']['single']
            
        drink_object = EspressoDrink(milk_mL, coffee_grams, water_mL, order_size)
        
        self._drink_list[drink_name] = drink_object
    
    def calculate_grams_of_coffee_drink(self, drink_recipe: dict):
        espresso_ratio = drink_recipe.get('espresso_ratio')
        milk_ratio = drink_recipe.get('milk_ratio')
        mL = drink_recipe.get('mL')
            
        mL_espresso = mL * espresso_ratio / (espresso_ratio + milk_ratio)
        mL_coffee = mL_espresso * (1/3)
            
        # .54 grams of coffee converts to 1 mL of coffee
        grams_coffee = mL_coffee * .54

        return grams_coffee
    
    def calculate_mL_of_water_drink(self, drink_recipe: dict):
        espresso_ratio = drink_recipe.get('espresso_ratio')
        milk_ratio = drink_recipe.get('milk_ratio')
        mL = drink_recipe.get('mL')
            
        mL_espresso = mL * espresso_ratio / (espresso_ratio + milk_ratio)
        mL_water = mL_espresso * (2/3)
        
        return mL_water
    
    def calculate_mL_of_milk_drink(self, drink_recipe: dict):
        espresso_ratio = drink_recipe['espresso_ratio']
        milk_ratio = drink_recipe['milk_ratio']
        mL = drink_recipe['mL']
        
        mL_milk = mL * milk_ratio / (espresso_ratio + milk_ratio)
        
        return mL_milk
    
    def calculate_grams_of_coffee_other(self, drink_recipe: dict):
        coffee_ratio = drink_recipe['coffee_ratio']
        water_ratio = drink_recipe['water_ratio']
        mL_single = drink_recipe['mL']['single']
        
        mL_coffee = mL_single * coffee_ratio / (coffee_ratio + water_ratio)
        
        # .54 grams of coffee converts to 1 mL of coffee
        grams_coffee = mL_coffee * .54
        
        return grams_coffee
    
    def calculate_mL_of_water_other(self, drink_recipe: dict):
        coffee_ratio = drink_recipe['coffee_ratio']
        water_ratio = drink_recipe['water_ratio']
        mL_single = drink_recipe['mL']['single']
        
        mL_water = mL_single * water_ratio / (coffee_ratio + water_ratio)
        
        return mL_water
    
    def calculate_mL_of_milk_other(self, drink_recipe: dict):
        mL_milk = 0.0
        return mL_milk

    def time_to_create_drink(self, drink_name: str):        
        # ideally, get_drink_params should also return the order size so that this isn't necessary
        drink = self._drink_list[drink_name]
        
        ingredients = [
          drink._coffee,
          drink._milk,
          drink._water
        ]

        time_sec = ((1/8) * drink._orderSize) + (5 * np.count_nonzero(ingredients))

        return time_sec