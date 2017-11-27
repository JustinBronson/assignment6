#Created by: Justin Bronson
#Created on: Nov 2017
#Created for ICS3U
#This program is a virtual game of 21


#from PIL import Image
import ui
import os
import random


userCards = []
compCards = []
dealtCards = []
cardvalues = []

#print(ndarray.sum(test[0:len(test)]))
#initalize arrays
deck = (os.listdir('./assets/deck'))

for card in deck:
    sections = card.split('_')
    print(sections[0])
    
    try:
        cardvalues.append(int(sections[0]))
    except:
        cardvalues.append(10)

#print cardvalues
print (deck)
#print (len(deck))
#print cardvalues
#print (len(cardvalues))

def card_dealer():
    #print len(cards)
    #print len(dealtCards)
    cardDealt = random.randint(0,51)
    while cardDealt in dealtCards:
        #print(cardDealt)
        cardDealt = random.randint(0,51)
    dealtCards.append(cardDealt)
    return cardDealt

def card_sum(cards):
    #sum of all the card
    cardSum = 0
    for card in cards:
        cardSum = cardSum + cardvalues[card]
        #print cardvalues[card]
    return cardSum
    
def start_game():
    #for x in dealtCards:
    del dealtCards[0:len(dealtCards)]
    
    del compCards[0:len(compCards)]
    del userCards[0:len(userCards)]
    
    view['compCardOne_image'].image = None
    view['compCardTwo_image'].image = None
    view['compCardThree_image'].image = None
    
    view['answer_label'].text = ' '
    view['userCardSum_label'].text = ' '
    view['compCardSum_label'].text = ' '
    
    userCards.append(card_dealer())
    userCards.append(card_dealer())
    #print userCards
    #print deck[userCards[0]]
    #print './assets/deck/' + deck[userCards[0]]
    
    view['userCardOne_image'].image = ui.Image('./assets/deck/' + deck[userCards[0]])
    view['userCardTwo_image'].image = ui.Image('./assets/deck/' + deck[userCards[1]])
    view['userCardThree_image'].image = None
    
    #to do disable play again button
    view['play_again_button'].enabled = False
    
    #to do enable extra card and check buttons
    view['extra_button'].enabled = True
    view['check_button'].enabled = True

def check_button_touch_up_inside(sender):
    calculate_winner(False)	

def extra_button_touch_up_inside(sender):
    calculate_winner(True)	
	
def play_again_button_touch_up_inside(sender):
    start_game()
	
def calculate_winner(extraCard):
    #to do disable play again button
    view['play_again_button'].enabled = True
    
    #to do enable extra card and check buttons
    view['extra_button'].enabled = False
    view['check_button'].enabled = False
    
    
    #to do extra card logic
    if extraCard == True:
        userCards.append(card_dealer())
        userCardThree = card_dealer()
        view['userCardThree_image'].image = ui.Image('./assets/deck/' + deck[userCards[2]])
    else:
        userCardThree = 0
    
    compCards.append(card_dealer())
    compCards.append(card_dealer())
    compCards.append(card_dealer())
    
    compCardSum = card_sum(compCards)
    userCardSum = card_sum(userCards)
    
    view['compCardOne_image'].image = ui.Image('./assets/deck/' + deck[compCards[0]])
    view['compCardTwo_image'].image = ui.Image('./assets/deck/' + deck[compCards[1]])
    view['compCardThree_image'].image = ui.Image('./assets/deck/' + deck[compCards[2]])
    
    view['compCardSum_label'].text = 'Computer score: ' + str(compCardSum)
    view['userCardSum_label'].text = 'Your score: ' + str(userCardSum)
    
    if compCardSum > 21 or userCardSum > 21:
        if compCardSum > 21 and userCardSum > 21:
            view['answer_label'].text = 'You tied'
        elif compCardSum > 21:
            view['answer_label'].text = 'You win'
        else:
            view['answer_label'].text = 'You lose'
    elif userCardSum == compCardSum:
        view['answer_label'].text = 'You tied'
    elif userCardSum > compCardSum:
        view['answer_label'].text = 'You win'
    else:
        view['answer_label'].text = 'You lose'

view = ui.load_view()
start_game()
view.present('sheet')
