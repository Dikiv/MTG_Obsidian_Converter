import requests


#Scryfall api
def get_img_uri(card_name,set_code):
  #set_code = 'fdn'
  url = f"https://api.scryfall.com/cards/named?exact={card_name}"
  try:
    if set:
        jsonResponse = requests.get(url,params={'set':set_code}).json()
    else:
        jsonResponse = requests.get(url).json()
    card_uri = jsonResponse['image_uris']["normal"]
    return card_uri
  except Exception as e:
    print(e)
  return ""
  


