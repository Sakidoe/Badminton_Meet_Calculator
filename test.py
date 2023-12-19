

# Your previous Plain Text content is preserved below:

#  * this is a two player card game
#  * the game starts with a deck of 52 cards represented as
#    unique integers [1...52]
#  * the cards are randomly shuffled and then dealt out to both players evenly.
#  * on each turn:
#      * both players turn over their top-most card
#      * the player with the higher valued card takes
#        the cards and puts them in their win pile
#        (scoring 1 point per card)
#  * this continues until all the players have no cards left
#  * the player with the highest score (number of cards in their win pile) wins.
#     * if they have the same number of cards in their win pile, tiebreaker goes to the player with the highest card in their win pile.

# * Be able to play the game with N players.
# * An input to the game will now be a list of strings (of length N) indicating the player names.
# * The deck contains M cards of distinct integers. It is not guaranteed M % N == 0. If there are leftover cards they should randomly be handed out to remaining players.
# i.e. with 17 cards and 5 people: 2 people get 4 cards and 3 get 3 cards
# For example the input: game(["Joe", "Jill", "Bob"], 5) would be a game between 3 players and 5 cards.
# * you should print the name of the player that won the game.
 

import random


def deck_sort(player_names, card_numbers):
    deck = []
    for i in range(1, card_numbers+1):
        deck.append(i)
    for i in range(0, card_numbers):
        s1 = random.randint(0,card_numbers-1)
        s2 = random.randint(0,card_numbers-1)
        temp = deck[s1]
        deck[s1] = deck[s2]
        deck[s2] = temp
    #print(deck)
    return deck

def distribute_player1(deck, player_names, player_decks, num_players):
    for i in range(0, num_players):
        player_decks[player_names[i]]= []
    for i in range(0, len(deck)):
        temp_num = i % num_players
        player_decks[player_names[temp_num]].append(deck[i])
    return player_decks

def play_game(player_decks, player_names, num_players):
    player_scores = dict()
    iterate_len = 0
    for i in range(0, num_players):
        player_scores[player_names[i]] = []
        temp = len(player_decks[player_names[i]])
        if temp > iterate_len:
            iterate_len = temp
    #print(iterate_len)
    for j in range(0, iterate_len):
        x_players = 0
        for m in range(0, num_players):
            if len(player_decks[player_names[m]]) > j:
                x_players+=1
        counter = 0
        temp_num = 0
        for k in range(0,x_players):
            if player_decks[player_names[k]][j] > temp_num:
                temp_num = player_decks[player_names[k]][j]
                counter = k
        for n in range(0, x_players):
            player_scores[player_names[counter]].append(player_decks[player_names[n]][j])
    print(player_scores)
    return player_scores


def check52(num_players, player_names, player_decks,deck, player_scores):
    for i in range(0, num_players):
        for j in player_scores[player_names[i]]:
            if j == len(deck):

                return player_names[i]
def check_winner(player_decks, player_names, num_players, player_scores, deck):
    highest_points = 0
    winner_names = []

    for key, value in player_scores.items():
        temp = len(value)
        if temp > highest_points:
            highest_points = temp
            #print(highest_points)
    for key2, value2 in player_scores.items():
        temp2 = len(value2)
        if temp2 == highest_points:
            winner_names.append(key2)
    if len(winner_names) > 1:
        print("tie")
        winner = check52(num_players, winner_names, player_decks, deck, player_scores)
    else:
        winner = winner_names[0]
    print(winner,"won!")
    #for i in ran
    # if player_scores["player1"] > player_scores["player2"]:
    #     print("player1 wins!")
    # elif player_scores["player2"] > player_scores["player1"]:
    #     print("player2 wins!")
    # else:
    #     if highest_card == 0:
    #         print("player1 wins!")
    #     if highest_card == 1:
    #         print("player2 wins!")
    #pass
#game(["Joe", "Jill", "Bob"], 5)


names = ["Joe", "Jill", "Bob"]
player_decks = dict()
cn = 29
num_players = len(names)
d = deck_sort(names, cn)
pd = distribute_player1(d, names, player_decks, num_players)
scores = play_game(pd,names, num_players)
#hc = check52(num_players, names, player_decks, d, scores)
check_winner(pd, names, num_players, scores,d)




