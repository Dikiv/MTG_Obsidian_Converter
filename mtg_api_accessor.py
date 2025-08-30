#from mtgsdk import Card
import requests
import json
from urllib.parse import urlparse
#Scryfall api

def get_img_uri(mtgo_id):
  
  try:
    url = "https://api.scryfall.com/cards/mtgo/"+str(mtgo_id)
    jsonResponse = requests.get(url).json()
    card_uri = jsonResponse['image_uris']["normal"]
    return card_uri
  except Exception as e:
    print(e)
  return ""
  


