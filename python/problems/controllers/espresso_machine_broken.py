from typing import List
import random
from .espresso_machine import EspressoMachine

class EspressoMachineBroken(EspressoMachine):
  def __init__(self, drink_list: dict = None):
    super().__init__(drink_list)
    pass

  def get_drink_params(self, drink_name: str) -> List[float]:
    if random.random() < 0.1:
      return [None, None, None]
    else:
      return super().get_drink_params(drink_name)

  