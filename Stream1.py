import time
import sys
import random
from random import randrange
import os

intro = "Welcome to the code from the first NMM stream!\nIn this program, we have several quick little fun scripts that we wrote during a Twitch live stream.\nEnjoy!"
game_menu = ["welcome message", "welcomemessage", "1", "1.", "2", "2.", "cat", "draw cat", "draw cat!", "3", "3.", "tic tac toe", "tic-tac-toe", "4", "4.", "deck", "deck of cards", "cards"]
game_welcome = ["welcome message", "welcomemessage", "1", "1."]
game_cat = ["2", "2.", "cat", "draw cat", "draw cat!"]
game_tic_tac_toe = ["3", "3.", "tic tac toe", "tic-tac-toe"]
game_deck_of_cards = ["4", "4.", "deck", "deck of cards", "cards"]
game_menu_text = "Please choose from the following options:\n1. Welcome Message\n2. Draw cat!\n3. Tic-Tac-Toe\n4. Deck of cards"

def text_printer(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        seconds = "0.0" + str(randrange(3, 4, 3))
        seconds = float(seconds)
        time.sleep(seconds)

def welcome_message():

    print("\nThe following was what was printed as the welcome message for my Twitch stream.")
    print("")
    print("\nHello Twitch!")
    print("Today I will attempt to write any terrible Python code ideas that you give me!")
    print("I code pretty much entirely in Python but I am just a hobbyist and an amateur so please forgive me if I make some basic mistakes!")
    print("Today I'll just be limiting myself to code that can be run and interacted with entirely in the terminal below.")
    print("So give me all your suggestions in the chat!")
    print("")
    #print("Find NotMyMajor on YouTube and GitHub! Use Nightbot commands !youtube and !github for links!")
    print("")
    print("")

def give_me_suggestions():
    text1 = "Give me suggestions in chat!\n"
    text_printer(text1)

def real_life_cat():
    
    text2 = "    /\_____/\ \n"
    text3 = "   /  o   o  \ \n"
    text4 = "  ( ==  ^  == )\n"
    text5 = "   )         (\n"
    text6 = "  (           )\n"
    text7 = " ( (  )   (  ) )\n"
    text8 = "(__(__)___(__)__)\n\n"
        
    text_printer(text2)
    text_printer(text3)
    text_printer(text4)
    text_printer(text5)
    text_printer(text6)
    text_printer(text7)
    text_printer(text8)

def deck_cards():
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suits = ["Spades", "Diamonds", "Clubs", "Hearts"]
    while True:
        rand_val = values[random.randrange(13)]
        rand_suit = suits[random.randrange(4)]
        print("{} of {}\n".format(rand_val, rand_suit))
        time.sleep(0.5)

def print_board(board):
  top, middle, bottom = board[0], board[1], board[2]
  print(f'_{top[0]}_|_{top[1]}_|_{top[2]}_')
  #print(f'_____')
  print(f'_{middle[0]}_|_{middle[1]}_|_{middle[2]}_')
  #print(f'_____')
  print(f' {bottom[0]} | {bottom[1]} | {bottom[2]} ')

def check_winner(board, player):
    game_over = False
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        
        game_over = True
    elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
        
        game_over = True
    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        
        game_over = True
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        
        game_over = True
    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        
        game_over = True
    elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
        
        game_over = True
  
    return(game_over)

def tic_tac_toe():
    blank_board = "__|__|__\n__|__|__\n  |  |  \n"
    #board = [["_","","_","|","_","","_","|","_","","_"],["_","","_","|","_","","_","|","_","","_"],[" ",""," ","|"," ",""," ","|"," ",""," "]]
    moves_chart = {
        "tl" : "0,0",
        "tm" : "0,1",
        "tr" : "0,2",
        "ml" : "1,0",
        "mm" : "1,1",
        "mr" : "1,2",
        "bl" : "2,0",
        "bm" : "2,1",
        "br" : "2,2"
    }
    available_moves = ["tl","tm","tr","ml","mm","mr","bl","bm","br"]
    options = "You can move to top left (tl), top middle (tm), top right (tr), middle left (ml), middle middle (mm), middle right (mr), bottom left (bl), bottom middle (bm), or bottom right (br)"
    board = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
    print(blank_board)
    print(options)
    cur_player = 'X'
    game_finish = False
    while not game_finish:
        move = input("What would you like your move to be?\n").strip().lower()
        while move not in available_moves:
            print("That's not an option.")
            print(options)
            move = input("What would you like your move to be?\n").strip().lower()
        move_place = moves_chart.get(move)
        # 0, 0 is the top left of the board
        y, x = map(int, move_place.strip().split(','))
        board[y][x] = cur_player
        print_board(board)
        available_moves.remove(move)
        game_finish = check_winner(board, cur_player)
        if game_finish:
            print("{} Wins!".format(cur_player))
        if len(available_moves) == 0:
            print("Tie!")
            game_finish = True
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'
           

def main():
    
    tic_tac_toe_yn = False
    welcome_message_yn= False
    deck_cards_yn = False
    give_me_suggestions_yn = False
    cat_yn = False

    
    print(game_menu_text)
    games_choice = input("Enter choice number or name here: ").lower().strip()
    while games_choice not in game_menu:
        print("That's not an option!")
        print(game_menu_text)
        games_choice = input("Enter choice number or name here: ").lower().strip()
    
    if games_choice in game_welcome:
        welcome_message_yn = True
    
    elif games_choice in game_cat:
        cat_yn = True
    
    elif games_choice in game_tic_tac_toe:
        tic_tac_toe_yn = True
    
    else:
        deck_cards_yn = True

    if tic_tac_toe_yn:
        tic_tac_toe()
    if welcome_message_yn and give_me_suggestions_yn:
        while True:
            welcome_message()
            time.sleep(17)
            for i in range(5):
                give_me_suggestions()
                time.sleep(1)
                print("")
                real_life_cat()
                time.sleep(1)
                print("")
    
    elif welcome_message_yn:
        while True:
            welcome_message()
            time.sleep(15)
            for i in range(5):
                real_life_cat()

    elif deck_cards_yn:
        deck_cards()
    
    elif cat_yn:
        while True:
            real_life_cat()

    input("Press ENTER to exit: ")
    
if __name__ == "__main__":
    main()