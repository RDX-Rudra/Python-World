import random

def deck():
    cardList = []
    for i in suits:
        for j in ranks:
            cardList.append(j + " of " + i)
    
    return cardList

def play(cardList):
    print("Dealing ...")
    player = random.choices(cardList, k=5)
    for k in player:
        cardList.remove(k)
    print("There are " , len(cardList) ," cards in the deck.")
    print("Player has the following cards in their hand: ")
    print(player)
    
    return player
    
    
suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
fdec = deck()
print(fdec)
print("There are " , len(fdec) ," cards in the deck.")
hand = play(fdec)


# problem 2

with open('Text1.txt', 'w+') as f:
    newDeck = deck()
    for ele in newDeck:
        f.write("%s\n" % ele)
    f.seek(0)
    print(len(f.readlines()))
      
    f.close
  
# problem 3
    
try:
    with open('Text1.txt', 'r') as f:
        card_dict = {}
        for key, line in enumerate(f):
            card_dict[key] = line.strip()

    print(card_dict)

except FileNotFoundError:
    print("File not found. Please make sure 'Text1.txt' exists.")
except Exception as e:
    print(f"An error occurred: {e}")
   
# problem 4
   
try:
    with open('Text1.txt', 'r') as f:
        cards_list = [(key, line.strip()) for key, line in enumerate(f)]

    print(cards_list)

except FileNotFoundError:
    print("File not found. Please make sure 'Text1.txt' exists.")
except Exception as e:
    print(f"An error occurred: {e}")
