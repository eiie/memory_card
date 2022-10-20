import sm
from os import listdir

# init var (conf)
decks_path = "decks"
card_parameters = ['question', 'answer', 'example', 'tags']
date_format = "%Y-%m-%d"

again = 1
user_input = 0

while again == 1:
    user_input = input('Choix : \n1 - Tout réviser \n2 - Paquets \n3 - Tags\n')
    if user_input in ['1', '2', '3']:
        again = 0


match user_input:
    case "1":
        cards_total = sm.list_cards_all(decks_path)
        cards_to_review = sm.is_it_review_time(cards_total)
        print(str(len(cards_to_review)) + '/' + str(len(cards_total)))
        # sm.display_cards(cards)
        question_number = 1
        for card in cards_to_review:
            card_question, card_answer, card_example, card_tags = sm.display_card(card)
            print(str(question_number) + '/' + str(len(cards_to_review)) + ' : ' + card_question)
            input()
            print(card_answer)
            print(card_example)
            print()
            again = 1
            while again == 1:
                quality = input('Qualité de la réponse [1-5] : ')
                if quality in ['1', '2', '3', '4', '5']:
                    again = 0
            sm.update_sm2_parameters(card, quality)
            question_number += 1

    case "2":
        decks = listdir(decks_path)
        for d in decks:
            cards_total = sm.list_cards_deck(decks_path, d)
            cards_to_review = sm.is_it_review_time(cards_total)
            print(' --- ' + d + ' (' + str(len(cards_to_review)) + '/' + str(len(cards_total)) + ')')

    case "3":
        print('b')
