import requests


#Scryfall api
def get_img_uri(card_name,set):
  url = "https://api.scryfall.com/cards/named?exact="+str(card_name)
  try:
    if set:
        jsonResponse = requests.get(url,params={'set':set}).json()
    else:
        jsonResponse = requests.get(url).json()
    card_uri = jsonResponse['image_uris']["normal"]
    return card_uri
  except Exception as e:
    print(e)
  return ""
  


