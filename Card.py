class Card:
  def __init__(self, name, cmc, type, subtypes, color, set):
    self.name = name 
    self.cmc = cmc
    self.type = type
    if subtypes:
       self.subtypes = subtypes
    self.color = color
    self.set = set