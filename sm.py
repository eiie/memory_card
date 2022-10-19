from supermemo2 import SMTwo
from datetime import datetime
from os import listdir
import configparser

# init var (conf)
decks_path = "decks"
date_format = "%Y-%m-%d"






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
def list_cards_all(dir):
    decks = listdir(dir)
    cards_table = []
    for d in decks:
        cards = listdir(dir + "/" + d)
        for c in cards:
            c = dir + "/" + d + "/" + c
            cards_table.append(c)
    return(cards_table)


deck = "deck1"


# list all cards for a deck
def list_cards_deck(dir, deck_name):
    cards = listdir(dir + "/" + deck_name)
    cards_table = []
    for c in cards:
        c = dir + "/" + deck_name + "/" + c
        cards_table.append(c)
    return(cards_table)


tag = ['tag1', 'tag3']


# list all cards for one or multiple tags
def list_cards_tag(dir, tag):
    decks = listdir(dir)
    cards_table = []
    for d in decks:
        cards = listdir(dir + "/" + d)
        for c in cards:
            card_config = configparser.ConfigParser()
            card_config.read(dir + '/' + d + '/' + c)
            tags = card_config['Card']['tags']
            for t in tags.split(" "):
                if t in tag and c not in cards_table:
                    c = dir + "/" + d + "/" + c
                    cards_table.append(c)
    return cards_table


print('cards_all')
print(list_cards_all(decks_path))
print('cards_deck')
print(list_cards_deck(decks_path, deck))
print('cards_tag')
print(list_cards_tag(decks_path, tag))

print('is_it_review_time ? all')
print(is_it_review_time(list_cards_all(decks_path)))
print('is_it_review_time ? deck')
print(is_it_review_time(list_cards_deck(decks_path, deck)))
print('is_it_review_time ? tag')
print(is_it_review_time(list_cards_tag(decks_path, tag)))
print('display card')
print(display_cards((is_it_review_time(list_cards_all(decks_path)))))


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
#     - Afficher une carte
#         - Entrée : carte à afficher
#         - Sortie : Question, réponse, exemple
#         - Description : Afficher une carte dans l'ordre : question puis
#         réponse et exemple
#     - Créer une carte
#         - Entrée : carte à modifier, paramètre à modifier, valeur du paramètre
#         - Sortie : n/a
#         - Description : Créer une carte avec ses paramètres : question,
#         réponse, exemple, tag
#     - Mettre à jour une carte (Card)
#         - Entrée : carte à modifier, paramètre à modifier, valeur du paramètre
#         - Sortie : n/a
#         - Description : Mettre à jour une carte avec ses paramètres:
#         question, réponse, exmple, tag
#     - Mettre à jour une carte (SM2)
#         - Entrée : carte à modifier, qualité (1-5)
#         - Sortie : n/a
#         - Description : utilisation de la fonction SMtwo pour mettre  à jour
#         les paramètres SM2. Si la review_date est vide alors first_review
#         sinon on récupère les paramètres SM2 de la carte en entrée de la
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



# using default date date.today()
a = SMTwo.first_review(1)
b = SMTwo.first_review(2, "2022-09-22")
c = SMTwo.first_review(3, "2022-09-22")
d = SMTwo.first_review(4, "2022-09-22")
e = SMTwo.first_review(5, "2022-09-22")

print("first review")
print(a)
print(b)
print(c)
print(d)
print(e)

# aa = SMTwo(a.easiness, a.interval, a.repetitions).review(1)
aa = SMTwo(b.easiness, b.interval, b.repetitions).review(1, "2022-09-23")
bb = SMTwo(b.easiness, b.interval, b.repetitions).review(2, "2022-09-23")
cc = SMTwo(c.easiness, c.interval, c.repetitions).review(3, "2022-09-23")
dd = SMTwo(d.easiness, d.interval, d.repetitions).review(4, "2022-09-23")
ee = SMTwo(e.easiness, e.interval, e.repetitions).review(5, "2022-09-23")

print("second review")
print(aa)
print(bb)
print(cc)
print(dd)
print(ee)

aaa = SMTwo(aa.easiness, aa.interval, aa.repetitions).review(1)
bbb = SMTwo(bb.easiness, bb.interval, bb.repetitions).review(2, "2022-09-24")
ccc = SMTwo(cc.easiness, cc.interval, cc.repetitions).review(3, "2022-09-29")
ddd = SMTwo(dd.easiness, dd.interval, dd.repetitions).review(4, "2022-09-29")
eee = SMTwo(ee.easiness, ee.interval, ee.repetitions).review(5, "2022-09-24")

print("third review")
print(aaa)
print(bbb)
print(ccc)
print(ddd)
print(eee)

print("review date")
print(aaa.review_date)
print(bbb.review_date)
