from types import List
import random
from python.problems.controllers.espresso_machine import EspressoMachine

class EspressoMachineBroken(EspressoMachine):
  def __init__(self, drink_list: dict = None):
    super(self, drink_list)
    pass

  def get_drink_params(self, drink_name: str) -> List[float, float, float]:
    if random.random() < 0.1:
      return [None, None, None]
    else:
      return super.get_drink_params(drink_name)

  