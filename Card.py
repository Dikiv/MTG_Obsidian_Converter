class Cardc:
 def __init__(self, name, cmc, type, subtypes, color, set, imgUrl):
    self.name = name 
    self.cmc = cmc
    self.type = type
    self.set = set
    if subtypes:
       self.subtypes = subtypes
    if color:
        self.color = color
    else:
        self.color = 'C'
    if imgUrl:
        self.imgUrl = imgUrl