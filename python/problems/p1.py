import json
from prettytable import PrettyTable
from controllers.espresso_machine import EspressoMachine

if __name__ == "__main__":
  with open('data/drinks.json', 'r') as drink_file: 
    coffee_recipes = json.loads(drink_file.read())
  print(coffee_recipes)

  # TODO: 1a - display amount of coffee in a single shot of espresso
  espresso_recipe = coffee_recipes['espresso']
  
  coffee_ratio = espresso_recipe['coffee_ratio']
  water_ratio = espresso_recipe['water_ratio']
  mL_single = espresso_recipe['mL']['single']
  
  mL_coffee = mL_single * coffee_ratio / (coffee_ratio + water_ratio)

  # .54 grams of coffee converts to 1 mL of coffee
  grams_coffee = mL_coffee * .54
  
  coffee_in_espresso = grams_coffee
  print(f"The amount of coffee in a single shot of espresso is: {coffee_in_espresso}")
  # Output: The amount of coffee in a single shot of espresso is: 5.4 grams


  # TODO: 1b - display amount of water in a flat white
  flat_white_recipe = coffee_recipes['flat_white']

  espresso_amount = flat_white_recipe['espresso_amount']
  espresso_ratio = flat_white_recipe['espresso_ratio']
  milk_ratio = flat_white_recipe['milk_ratio']
  mL_total = flat_white_recipe['mL']
  
  # calculate espresso amount used
  # can this exact amount be made? assuming no here, but yes throughout the rest of assessment
  mL_espresso_used = mL_total * espresso_ratio / (espresso_ratio + milk_ratio)

  # calculate espresso amount made
  mL_espresso_made = espresso_recipe['mL']['double']
  mL_water = mL_espresso_made * water_ratio / (coffee_ratio + water_ratio)
  
  water_in_flat_white = mL_water
  print(f"The amount of water in a flat white is: {water_in_flat_white}")  

  # TODO: 1c (i) - print a table showing coffee / water / milk for each drink
  drinks_table = PrettyTable(['Drink Name', 'Coffee (grams)', 'Water (mL)', 'Milk (mL)', 'Time (sec)'])
  machine = EspressoMachine()
  list_of_drinks = ['ristretto', 'espresso', 'lungo', 'crema', 'cappuccino', 'latte', 'flat_white']

  for drink in list_of_drinks:
      machine.add_drink_to_menu(drink)
      [coffee, water, milk] = machine.get_drink_params(drink)
      time = machine.time_to_create_drink(drink)
      drinks_table.add_row([drink, coffee, water, milk, time])
  print(drinks_table)

  # Output:
  # +------------+--------------------+--------------------+-----------+------------+
  # | Drink Name |   Coffee (grams)   |     Water (mL)     | Milk (mL) | Time (sec) |
  # +------------+--------------------+--------------------+-----------+------------+
  # | ristretto  | 8.100000000000001  |        15.0        |    0.0    |   13.75    |
  # |  espresso  |        5.4         |        20.0        |    0.0    |   13.75    |
  # |   lungo    | 4.050000000000001  |        22.5        |    0.0    |   13.75    |
  # |   crema    | 2.0250000000000004 |       26.25        |    0.0    |   13.75    |
  # | cappuccino |        9.9         | 36.666666666666664 |   110.0   |   35.625   |
  # |   latte    |        14.4        | 53.33333333333333  |   160.0   |    45.0    |
  # | flat_white |        9.9         | 36.666666666666664 |   110.0   |   35.625   |
  # +------------+--------------------+--------------------+-----------+------------+

  # TODO: 1c (ii) - add drink to menu
  # Used in 1c (i)

  # TODO: 1c (iii) - implement time component to create each drink
  # Used in 1c (i)
