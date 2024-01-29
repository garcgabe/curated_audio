import json
import requests

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

    card_info_response = requests.post('http://127.0.0.1:8765', json={'action': "cardsInfo", 'params': {"cards": all_card_ids}, 'version': 6})
    print(response.status_code)
    card_info_response_data = response.json()
    print(card_info_response_data.items())
