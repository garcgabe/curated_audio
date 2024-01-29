import json
import requests

deck_names = ["1001 Most Useful Spanish Words and Sentences (TTS accurate)",\
              "spanish 7500 intermediate/advanced sentences"]

if __name__=="__main__":

    # then find all cards in these decks
    # -- findCards, params = "deck": "name"
    # then get all the card data for these cards
    # -- cardsInfo, params = "cards": [ids as ints]
    all_card_ids = []

    action = "findCards"
    params = { "query": "*" }

    print(params)

    response = requests.post('http://127.0.0.1:8765', json={'action': action, 'params': params, 'version': 6})
    print(response.status_code)
    response_data = response.json()
    print(json.dumps(response.data.items(), indent=4) )