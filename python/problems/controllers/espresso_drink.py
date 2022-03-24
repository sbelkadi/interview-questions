class EspressoDrink:
  def __init__(self, milk: float, coffeeBeans: float, water: float, orderSize: float = None): 
    """
    milk: amount of milk in mL
    coffeeBeans: coffeeBeans in grams
    water: amount of water in mL
    orderSize: size of drink order in oz
    """
    self._milk = milk
    self._coffee = coffeeBeans
    self._water = water
    self._orderSize = orderSize

  @property
  def orderSize(self):
    return self._ordersize

  @orderSize.setter
  def orderSize(self, value):
    self._ordersize = value