#from mtgsdk import Card
import requests

#Scryfall api

def get_img_uri(mtgo_id):
  try:
    jsonResponse = requests.get("https://api.scryfall.com/cards/mtgo/"+mtgo_id).json()
    card_uri = jsonResponse['image_uris']["normal"]
  except Exception:
    print(Exception.with_traceback)

  return card_uri


