from supermemo2 import SMTwo
import configparser

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

aa = SMTwo(a.easiness, a.interval, a.repetitions).review(1)
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

# Create a card from scratch (question, answer, tags)
# Modify  a card (question / answer / tags (add, remove))
config = configparser.ConfigParser()
config['Card'] = {'question': 'This is a question ?',
                  'answer': 'This is the answer.',
                  'example': 'This is an example.',
                  'tags': 'tag1, tag2'}
config['SM2_Parameters'] = {'easiness': '1',
                            'interval': '0',
                            'repetitions': '17',
                            'review_date': '2022-09-24'}
with open('card2', 'w') as cardfile:
    config.write(cardfile)


# Review a deck with SM2 algorithm
## Grep review_date parameter for each card and compare with current date
# Review an entire deck

## Review a card
### Display Question
### Display Answer and ask for quality (1-5)
### Update card parameters (with SMTwo function results and current date)

# Choose deck
## 1 level directory : deck
## - deck1
##   - card
##   - card
## - deck2
##   - card

# https://github.com/alankan886/SuperMemo2
# https://docs.python.org/3/library/configparser.html
