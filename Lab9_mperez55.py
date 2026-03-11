''''Name: Lab9_mperez55
Author: Marvin Perez
Purpose: Match coins game lab 9.
Date: 03/10/2026'''
from player import player

def main():
    player1 = player("Player 1")
    player2 = player("Player 2")

    print(f"{player1.get_name()} has {player1.get_wallet()} coins")
    print(f"{player2.get_name()} has {player2.get_wallet()} coins")

    play = input("\nDo you want to toss the coins? y/n")

    while  play == "y":

        player1.toss_coin()
        player2.toss_coin()

        print(f"\n{player1.get_name()} tossed {player1.get_coin_side()}")
        print(f"{player2.get_name()} tossed {player2.get_coin_side()}")


        if player1.get_coin_side() == player2.get_coin_side():
            print(f"\nCoins match!\n{player1.get_name()} wins a coin and {player2.get_name()} loses a coin")
            player1.win_coin()
            player2.lose_coin()


        else:
            print(f"\nCoins don't match!\n{player2.get_name()} wins a coin and {player1.get_name()} loses a coin")
            player2.win_coin()
            player1.lose_coin()

        print(f"\n{player1.get_name()} has {player1.get_wallet()} coins")
        print(f"{player2.get_name()} has {player2.get_wallet()} coins")

        play = input("Do you want to toss the coins? y/n\n")
    
    print(f"\n---Final Score---\n{player1.get_name()} has {player1.get_wallet()} coins\n{player2.get_name()} has {player2.get_wallet()} coins")
    if player1.get_wallet() == player2.get_wallet():
        print("\nIts' a draw!")
    elif player1.get_wallet() > player2.get_wallet():
        print(f"\n{player1.get_name()} wins!")
    else:
        print(f"\n{player2.get_name()} wins!")
main()