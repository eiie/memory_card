from supermemo2 import SMTwo
from datetime import datetime
from os import listdir
from os import path
import configparser

# init var (conf)
decks_path = "decks"
card_parameters = ['question', 'answer', 'example', 'tags']
date_format = "%Y-%m-%d"


# create a card in a deck
def create_card(decks_path, deck_name, question, answer, example, tags):
    file_path = str(decks_path) + "/" + str(deck_name) + "/" + datetime.now().strftime("%Y%m%d%H%M%S")
    sm2_parameters = SMTwo.first_review(1)
    card_config = configparser.ConfigParser()
    card_config['Card'] = {'question': question,
                           'answer': answer,
                           'example': example,
                           'tags': tags}
    card_config['SM2_Parameters'] = {'easiness': sm2_parameters.easiness,
                                     'interval': sm2_parameters.interval,
                                     'repetitions': sm2_parameters.repetitions,
                                     'review_date': sm2_parameters.review_date}
    if not path.exists(file_path):
        with open(file_path, 'w') as card_file:
            card_config.write(card_file)


quality = 5


# update card parameters : question, answer, example or tag
def update_card_parameters(card, parameter, parameter_value):
    for c in card:
        if parameter in card_parameters:
            card_config = configparser.ConfigParser()
            card_config.read(card)
            card_config.set('Card', str(parameter), str(parameter_value))
            with open(card, 'w') as card_file:
                card_config.write(card_file)


# update SMTwo parameters : easiness, interval, repetitions and review_date
def update_sm2_parameters(card, quality):
    for c in card:
        card_config = configparser.ConfigParser()
        card_config.read(c)
        card_easiness = card_config['SM2_Parameters']['easiness']
        card_interval = card_config['SM2_Parameters']['interval']
        card_repetitions = card_config['SM2_Parameters']['repetitions']
        sm2_parameters = SMTwo(float(card_easiness), int(card_interval), int(card_repetitions)).review(quality)
        card_config.set('SM2_Parameters', 'easiness', str(sm2_parameters.easiness))
        card_config.set('SM2_Parameters', 'interval', str(sm2_parameters.interval))
        card_config.set('SM2_Parameters', 'repetitions', str(sm2_parameters.repetitions))
        card_config.set('SM2_Parameters', 'review_date', str(sm2_parameters.review_date))
        with open(c, 'w') as card_file:
            card_config.write(card_file)


# display a card
def display_cards(card):
    for c in card:
        card_config = configparser.ConfigParser()
        card_config.read(c)
        card_question = card_config['Card']['question']
        card_answer = card_config['Card']['answer']
        card_example = card_config['Card']['example']
        card_tags = card_config['Card']['tags']
        print('question:', card_question)
        print('answer:', card_answer)
        print('example:', card_example)
        print('tags:', card_tags)


# list cards ready for review
def is_it_review_time(card):
    cards_table = []
    for c in card:
        card_config = configparser.ConfigParser()
        card_config.read(c)
        r_date = card_config['SM2_Parameters']['review_date']
        r_diff_day = ((datetime.now() - datetime.strptime(r_date, date_format)).days)
        if r_diff_day >= 0:
            cards_table.append(c)
    return cards_table


# list all cards
def list_cards_all(decks_path):
    decks = listdir(decks_path)
    cards_table = []
    for d in decks:
        cards = listdir(decks_path + "/" + d)
        for c in cards:
            c = decks_path + "/" + d + "/" + c
            cards_table.append(c)
    return(cards_table)


deck = "deck1"


# list all cards for a deck
def list_cards_deck(decks_path, deck_name):
    cards = listdir(decks_path + "/" + deck_name)
    cards_table = []
    for c in cards:
        c = decks_path + "/" + deck_name + "/" + c
        cards_table.append(c)
    return(cards_table)


tag = ['tag1', 'tag3']


# list all cards for one or multiple tags
def list_cards_tag(decks_path, tag):
    decks = listdir(decks_path)
    cards_table = []
    for d in decks:
        cards = listdir(decks_path + "/" + d)
        for c in cards:
            card_config = configparser.ConfigParser()
            card_config.read(decks_path + '/' + d + '/' + c)
            tags = card_config['Card']['tags']
            for t in tags.split(" "):
                if t in tag and c not in cards_table:
                    c = decks_path + "/" + d + "/" + c
                    cards_table.append(c)
    return cards_table


# print('cards_all')
# print(list_cards_all(decks_path))
# print('cards_deck')
# print(list_cards_deck(decks_path, deck))
# print('cards_tag')
# print(list_cards_tag(decks_path, tag))

# print('is_it_review_time ? all')
# print(is_it_review_time(list_cards_all(decks_path)))
# print('is_it_review_time ? deck')
# print(is_it_review_time(list_cards_deck(decks_path, deck)))
# print('is_it_review_time ? tag')
# print(is_it_review_time(list_cards_tag(decks_path, tag)))
# print('display card')
# print(display_cards((is_it_review_time(list_cards_all(decks_path)))))
# print('update sm2 parameters')
# print(update_sm2_parameters(((is_it_review_time(list_cards_all(decks_path)))), quality))
# print('update card parameters')
# update_card_parameters('decks/deck1/card1', 'question', 'quetol')
# print('create a card')
# create_card(decks_path, "deck2", "a", "b", "c", "d")

# Create a card from scratch (question, answer, tags)
# Modify  a card (question / answer / tags (add, remove))
## Increment card number
# config = configparser.ConfigParser()
# config['Card'] = {'question': 'This is a question ?',
#                   'answer': 'This is the answer.',
#                   'example': 'This is an example.',
#                   'tags': 'tag1, tag2'}
# config['SM2_Parameters'] = {'easiness': '1',
#                             'interval': '0',
#                             'repetitions': '17',
#                             'review_date': '2022-09-24'}


# https://github.com/alankan886/SuperMemo2
# https://docs.python.org/3/library/configparser.html


# Ecrans :
# - Tout réviser (afficher nombre de carte à réviser et le nombre de carte totale)
#         - Revue des cartes une par une (question, réponse et exemple, qualité) + option modifier
# - Paquets
#     - Choisir le paquet (afficher nombre de carte à réviser et le nombre de carte totale ainsi que les tags du paquets)
#         - Révision (SM2)
#             - Revue des cartes une par une (question, réponse et exemple, qualité) + option modifier
#         - Révision de tout le paquet
#             - Revue des cartes une par une (question, réponse et exemple, qualité) + option modifier
#         - Modifier le paquet
#             - Nom du paquet
#             - Liste des cartes (modifier)
# - Tags
#     - Choisir le/les tags (afficher nombre de carte à réviser et le nombre de
#       carte totale ainsi que les paquets correspondants)
#         - Révision (SM2)
#             - Revue des cartes une par une (question, réponse et exemple, qualité) + option modifier
#         - Révision de tout le(s) tag(s) sélectionné(s)
#             - Revue des cartes une par une (question, réponse et exemple, qualité) + option modifier
#         - Modifier le/les tags
#             - Nom du tag
#             - Liste des cartes (modifier)

# Fonctions :
#     + Afficher une carte
#         - Entrée : carte à afficher
#         - Sortie : Question, réponse, exemple
#         - Description : Afficher une carte dans l'ordre : question puis
#         réponse et exemple
#     + Créer une carte
#         - Entrée : carte à modifier, paramètre à modifier, valeur du paramètre
#         - Sortie : n/a
#         - Description : Créer une carte avec ses paramètres : question,
#         réponse, exemple, tag (SM2Parameters = first_review)
#     + Mettre à jour une carte (Card)
#         - Entrée : carte à modifier, paramètre à modifier, valeur du paramètre
#         - Sortie : n/a
#         - Description : Mettre à jour une carte avec ses paramètres:
#         question, réponse, exmple, tag
#     + Mettre à jour une carte (SM2)
#         - Entrée : carte à modifier, qualité (1-5)
#         - Sortie : n/a
#         - Description : utilisation de la fonction SMtwo pour mettre  à jour
#         les paramètres SM2. On récupère les paramètres SM2 de la carte en entrée de la
#         fonction SMtwo. On utilise la date actuelle pour mettre à  jour une
#         carte.
#     + Vérifier date de revue et compare à la date du jour
#         - Entrée : fichier à scanner
#         - Sortie : entier : différence en jour entre la date de revue et la
#         date actuelle
#         - Description : On récupère ici la différence entre la date du jour
#         et la date de la revue. Si la différence est >=0, la carte est à
#         réviser
#     + Liste des cartes par deck :
#         - Entrée : nom du deck
#         - Sortie : liste des cartes
#         - Description : On liste les cartes à réviser en récupérant la
#         review_date de chaque carte dans le dossier du deck et en utilisant la
#         fonction pour comparer les dates du jour et date de revue. (Création
#         d'une liste via un "list dir" puis comparaison de date de chaque carte pour créer une
#         deuxième liste)
#     + Liste les cartes à réviser par tag(s) :
#         - Entrée : liste des tags
#         - Sortie : liste des cartes
#         - Description : On liste les cartes à réviser en récupérant la
#         review_date de chaque carte par tags et en utilisant la fonction pour
#         comparer les dates du jour et date de revue. (
#     + Liste des cartes à réviser :
#         - Entrée : liste des cartes
#         - Sortie : liste des cartes à réviser
#         - Description : Comparaison de date de chaque carte pour créer la
#         liste via la fonction de comparaison (si entier >=0 populer la
#         nouvelle liste).

# Quality: The quality of recalling the answer from a scale of 0 to 5.
# 5: perfect response.
# 4: correct response after a hesitation.
# 3: correct response recalled with serious difficulty.
# 2: incorrect response; where the correct one seemed easy to recall.
# 1: incorrect response; the correct one remembered.
# 0: complete blackout.
# Easiness: The easiness factor, a multipler that affects the size of the interval, determine by the quality of the recall.
# Interval: The gap/space between your next review.
# Repetitions: The count of correct response (quality >= 3) you have in a row.
