class EspressoDrink:
  def __init__(self, milk: float, coffeeBeans: float, orderSize: DrinkSize = None): 
    """
    milk: amount of milk in mL
    coffeeBeans: coffeeBeans in grams
    orderSize: size of drink order in oz
    """
    self._milk = milk
    self._coffee = coffeeBeans
    self._orderSize = orderSize

  @property
  def orderSize(self):
    return self._ordersize

  @orderSize.setter
  def orderSize(self, value):
    self._ordersize = value

  
