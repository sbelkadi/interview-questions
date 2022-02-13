from types import List
from .espresso_drink import EspressoDrink

class EspressoMachine:
  def __init__(self, drink_list: dict = None):
    pass

  def get_drink_params(self, drink_name: str) -> List[float, float, float]:
    return NotImplementedError

  def add_drink_to_menu(self, drink_name: str):
    return NotImplementedError
