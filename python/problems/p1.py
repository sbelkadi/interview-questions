import json
from controllers.espresso_machine import EspressoMachine

if __name__ == "__main__":
  with open('data/drinks.json', 'r') as drink_file: 
    coffee_recipes = json.loads(drink_file.read())
  print(coffee_recipes)

  # TODO: 1a - display amount of coffee in a single shot of espresso
  coffee_in_espresso = None
  print(f"The amount of coffee in a single shot of espresso is: {coffee_in_espresso}")

  # TODO: 1b - display amount of water in a flat white
  water_in_flat_white = None
  print(f"The amount of water in a flat white is: {water_in_flat_white}")  

  # TODO: 1c (i) - print a table showing coffee / water / milk for each drink

  # TODO: 1c (ii) - add drink to menu

  # TODO: 1c (iii) - implement time component to create each drink
  
