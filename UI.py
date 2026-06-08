from tkinter import *
from PIL import Image, ImageTk
from WarGame import Player, Deck, Card
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

window = Tk()

new_deck = Deck()
new_deck.shuffle()

player_one = Player("Arinjay")
player_two = Player("Vedant")

for x in range(26):
    player_one.add_card(new_deck.deal_one())
    player_two.add_card(new_deck.deal_one())

window.geometry("800x600") # By this I can edit the GUI window size as per user convience.
window.title("War : The Card Game.")

img = Image.open("swordcr.png")
img = img.resize((50,50))

war_logo = ImageTk.PhotoImage(img)
window.iconphoto(True,war_logo)

window.config(background="#EEEBE6") # Here the _hashtag_ is important after the hexadecimal number

# Using frame to sandwich war between swords

top_frame = Frame(window,bg="#EEEBE6")
top_frame.pack(pady = 20)

# Sword image load

swordcr = war_logo

# For left sword
left_sword = Label(top_frame,image=swordcr,bg="#EEEBE6")
left_sword.pack(side=LEFT,padx=10)

# War Text
war_text = Label(
    top_frame,
    text="WAR",
    font=("Cinzel", 30, "bold"),
    fg="#1E140A",
    bg="#EEEBE6"
)
war_text.pack(side=LEFT, padx=10)

# Right sword 
right_sword = Label(top_frame,image=swordcr,bg="#EEEBE6")
right_sword.pack(side=LEFT,padx=10)

# Use side LEFT for both sword as LEFT makes the right sword to be placed at the right side
# Side RIGHT is used when we want to place something to the atmost right most extreme corner of the window.

left_sword.image = swordcr
right_sword.image = swordcr
# Here left_sword is an object in which the sword is store 
# To access the stored sword or to display it we used the '.' do access whats in that left_sword

# Player 1 & Player 2 names - RESPONSIVE POSITIONING

player_one_label = Label(window,text="Arinjay",fg="#1E140A",bg="#EEEBE6",font=("Times New Roman",18,"bold"))
player_one_label.place(relx=0.2, rely=0.42, anchor="center")

player_two_label = Label(window,text="Vedant",fg="#1E140A",bg="#EEEBE6",font=("Times New Roman",18,"bold"))
player_two_label.place(relx=0.8, rely=0.42, anchor="center")

# Player 1 count show
player_one_count = Label(window,text="Cards: 26",fg="#1E140A",bg="#EEEBE6",font=("Times New Roman",12,"bold"))
player_one_count.place(relx=0.2, rely=0.2, anchor="center")

# Round count text
round_num_label = Label(window,text="Round: ",fg="#1E140A",bg="#EEEBE6",font=("Times New Roman",18,"bold"))
round_num_label.place(relx=0.5, rely=0.2, anchor="center")

# Player 2 count show
player_two_count = Label(window,text="Cards: 26",fg="#1E140A",bg="#EEEBE6",font=("Times New Roman",12,"bold"))
player_two_count.place(relx=0.8, rely=0.2, anchor="center")

result_label = Label(window, text="", fg="#1E140A", bg="#EEEBE6",font=("Times New Roman",16,"bold"))
result_label.place(relx=0.5, rely=0.75, anchor="center")

def update_count():
    
    player_one_count.config(text = f"Cards: {len(player_one.deck)}")
    player_two_count.config(text = f"Cards: {len(player_two.deck)}")

player_one_card = Label(window,bg="#EEEBE6")
player_one_card.place(relx=0.2, rely=0.55, anchor="center")

player_two_card = Label(window,bg="#EEEBE6")
player_two_card.place(relx=0.8, rely=0.55, anchor="center")


rank_map = {
    'Two': '2', 'Three': '3', 'Four': '4', 'Five': '5',
    'Six': '6', 'Seven': '7', 'Eight': '8', 'Nine': '9',
    'Ten': '10', 'Jack': 'jack', 'Queen': 'queen',
    'King': 'king', 'Ace': 'ace'
}

def show_card(label,card):
    rank = rank_map[card.rank]
    suit = card.suit.lower()
    img = Image.open(f"cards/{rank}_of_{suit}.png")
    img = img.resize((80,120))
    photo = ImageTk.PhotoImage(img)
    
    label.config(image=photo)
    label.image = photo


player_one_cards = [] # This is basically the list of cards(of player 1) which are on the table 
# player_one.deck = the cards which player one has in his hands.
# player_two.deck = the cards which player two has in his hands.
player_two_cards = [] # This is basically the list of cards(of player 2) which are on the table

round_num = 0
at_war = False

def restart_game():
    global round_num, at_war, player_one, player_two, player_one_cards, player_two_cards

    round_num = 0
    at_war = False
    player_one_cards.clear()
    player_two_cards.clear()

    player_one = Player("Arinjay")
    player_two = Player("Vedant")

    new_deck = Deck()
    new_deck.shuffle()
    for x in range(26):
        player_one.add_card(new_deck.deal_one())
        player_two.add_card(new_deck.deal_one())

    update_count()
    round_num_label.config(text="Round: ")
    result_label.config(text="")
    player_one_card.config(image="")
    player_two_card.config(image="")
    button.config(state="normal")
    button2.config(state="normal")

def click():
    print("clicked")
    
    global round_num, at_war
    
    if len(player_one.deck) == 0 or len(player_two.deck) == 0:
        return
    
    round_num += 1
    round_num_label.config(text=f"Round: {round_num}")
    
    card1 = player_one.remove_card()# remove_card is basically =  deck.pop(0)
    card2 = player_two.remove_card()
    
    player_one_cards.append(card1)
    player_two_cards.append(card2)
    
    show_card(player_one_card, card1)
    show_card(player_two_card, card2)
    
    update_count()    
    
    # If player 1 wins the round he gets his as well as player 2 cards
    if player_one_cards[-1].value > player_two_cards[-1].value:
        for card in player_one_cards:
            player_one.add_card(card)
        for card in player_two_cards:
            player_one.add_card(card)
        player_one_cards.clear()
        player_two_cards.clear()
        update_count()
        
        if at_war:
            result_label.config(text="Arinjay Wins the War!")
            at_war = False
        else:
            result_label.config(text=f"Arinjay Wins {round_num} Round!")
        if len(player_two.deck) == 0:
            result_label.config(text="Arinjay Wins the Game!.")
            button.config(state="disabled")
            button2.config(state="disabled")    
            
    # If player 2 wins the round the he gets his as well as player 1 cards.
    elif player_two_cards[-1].value > player_one_cards[-1].value:
        for card in player_two_cards:
            player_two.add_card(card)
        for card in player_one_cards:
            player_two.add_card(card)
        player_one_cards.clear()
        player_two_cards.clear()
        update_count()
        
        if at_war:
            result_label.config(text="Vedant Wins the War!")
            at_war = False
        else:
            result_label.config(text=f"Vedant Wins {round_num} Round!")
        if len(player_one.deck) == 0:
            result_label.config(text="Vedant Wins the Game!.")
            button.config(state="disabled")
            button2.config(state="disabled")
        
    else:
        at_war = True
        
        if len(player_one.deck) < 5 and len(player_two.deck) < 5: # This case means both players have less than 5 cards and War just came then the one who has more cards but less than 5 wins the match.
            if len(player_one.deck) > len(player_two.deck):
                result_label.config(text="Arinjay Wins!")
            else:
                result_label.config(text="Vedant Wins!")
            at_war = False
            button.config(state="disabled")
            button2.config(state="disabled")
            return
                
        elif len(player_one.deck) <= 6:
            result_label.config(text="Vedant wins the WAR!.Arinjay is too weak to fight the war.")
            at_war = False
            button.config(state="disabled")
            button2.config(state="disabled")
            return
        
        elif len(player_two.deck) <= 6:
            result_label.config(text="Arinjay wins the WAR!.Vedant is too weak to fight the war.")
            at_war = False
            button.config(state="disabled")
            button2.config(state="disabled")
            return
        
        else:
            for _ in range(5): # This loop means I do not care about the iterartions I just want it to run 5 times that it.
                player_one_cards.append(player_one.remove_card())
                player_two_cards.append(player_two.remove_card())
            result_label.config(text="WAR! Draw again.")
            update_count()
        
            
img1 = Image.open("draw_card.png")
img1 = img1.resize((250,80))
p1 = ImageTk.PhotoImage(img1)

img2 = Image.open("new_card.png")
img2 = img2.resize((250,80))
p2 = ImageTk.PhotoImage(img2)  
  
button = Button(window,
                command=click,
                font=(30),
                image= p1,
                )

button2 = Button(window,
                 command = restart_game,
                 font = (30),
                 image = p2)


button.place(relx = 0.15, rely = 0.88, anchor = "center")
button2.place(relx = 0.85, rely = 0.88, anchor = "center")

window.mainloop()
