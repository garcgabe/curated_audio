import json
import requests

# separate testing found unique card IDs for all spanish anki cards i had in my decks
# card id ranges for cards in decks
# can call cardsInfo action to get a random card's information
DECK_ONE_CARD_ID_RANGES = (1367317476414, 1367317477593)

DECK_TWO_CARD_ID_RANGES = (1466793883066, 1466793890694)

deck_names = ["1001 Most Useful Spanish Words and Sentences (TTS accurate)",\
              "spanish 7500 intermediate/advanced sentences"]

if __name__=="__main__":

    # anki app needs to be running for Ankiconnect server to be running in background 
    # then get all the card data for these cards
    # -- cardsInfo, params = "cards": [ids as ints]

    card_info_response = requests.post('http://127.0.0.1:8765', json={'action': "cardsInfo", 'params': {"cards": all_card_ids}, 'version': 6})
    print(response.status_code)
    card_info_response_data = response.json()
    print(card_info_response_data.items())

    # for card in card_info_response_data:
    # card_front = card["fields"]["Front"]["value"]
    # card_back = card["fields"]["Back"]["value"]