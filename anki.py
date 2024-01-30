import json
import requests

# card id ranges for cards in decks
# can call cardsInfo action to get a random card's information
DECK_ONE_CARD_ID_RANGES = (1367317476414, 1367317477593)

DECK_TWO_CARD_ID_RANGES = (1466793883066, 1466793890694)

deck_names = ["1001 Most Useful Spanish Words and Sentences (TTS accurate)",\
              "spanish 7500 intermediate/advanced sentences"]

if __name__=="__main__":

    # then find all cards in these decks
    # -- findCards, params = "deck": "name"
    # then get all the card data for these cards
    # -- cardsInfo, params = "cards": [ids as ints]
 
    response = requests.post('http://127.0.0.1:8765', json={'action': "findCards", 'params': {"query": "*"}, 'version': 6})
    print(response.status_code)
    response_data = response.json()
    all_card_ids = response_data['result']

    card_info_response = requests.post('http://127.0.0.1:8765', json={'action': "cardsInfo", 'params': {"cards": random_card_id}, 'version': 6})
    print(response.status_code)
    card_info_response_data = response.json()
    print(card_info_response_data.items())

    # card_front = first["fields"]["Front"]["value"]
    # card_back = first["fields"]["Back"]["value"]