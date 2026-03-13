"""
Program: The Main Game Logic
Name: Dashawn Duncan
Purpose: Create a file that runs the game
Date: 3/13/2026
"""

from player import Player

def main():
    
    p1 = Player("Player 1")
    p2 = Player("Player 2")

    print("--- Coin Match Game ---")
    print(f"{p1.get_name()} has {p1.get_wallet()} coins.")
    print(f"{p2.get_name()} has {p2.get_wallet()} coins.\n")

    keep_playing = input("Do you want to toss the coins? (y/n): ").lower()

    while keep_playing == 'y':
        print("\nTossing...")
        
        
        p1.toss_coin()
        p2.toss_coin()

        side1 = p1.get_coin_side()
        side2 = p2.get_coin_side()

        print(f"{p1.get_name()} tossed {side1}")
        print(f"{p2.get_name()} tossed {side2}")

        
        if side1 == side2:
            print(f"...It's a Match! {p1.get_name()} wins a coin.")
            p1.win_coin()
            p2.lose_coin()
        else:
            print(f"...No Match! {p2.get_name()} wins a coin.")
            p2.win_coin()
            p1.lose_coin()

        print(f"\n{p1.get_name()} has {p1.get_wallet()} coins.")
        print(f"{p2.get_name()} has {p2.get_wallet()} coins.\n")

        if p1.get_wallet() <= 0 or p2.get_wallet() <= 0:
            print("Game Over! A player has run out of coins.")
            break

        keep_playing = input("Do you want to toss the coins? (y/n): ").lower()

  
    print("\n--- Final Score ---")
    score1 = p1.get_wallet()
    score2 = p2.get_wallet()
    print(f"{p1.get_name()}: {score1}")
    print(f"{p2.get_name()}: {score2}")

    if score1 > score2:
        print(f"{p1.get_name()} wins the game!")
    elif score2 > score1:
        print(f"{p2.get_name()} wins the game!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()