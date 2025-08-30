#A Script that reads magic card data from CSV files
#and creates a directory of sorted cards in .md files
#intended for obsidian bases.

from mtg_api_accessor import get_img_uri
from md_writer import md_writer
from Card import Card
import csv

class Card:
  def __init__(self, name, cmc, type, subtypes, color, set):
    self.name = name 
    self.cmc = cmc
    self.type = type
    if subtypes:
       self.subtypes = subtypes
    self.color = color
    self.set = set


with open('testcsv.csv', mode='r') as csvfile:
    reader = csv.reader(csvfile)
    
    #read categories of cards 
    row_0 = reader.__next__()
    for card_info in reader:

        
        #splitting up types
        types = card_info[2].split("-")
        mType = types[0].strip()
        
        sTypes = types[-1:][0].strip().split(" ")
        
        mtgo_id = print(card_info[15])
        img_uri = get_img_uri(mtgo_id)
        
        #Assign data to object
        card0 = Card(card_info[0],card_info[1],mType,sTypes,card_info[3],card_info[4])

        #Find/Make correct directory
        md_writer(card0,img_uri)

        




