import random

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def get_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def black_jack():
    print(logo)
    user_cards =[get_card(), get_card()]
    total_user_score = 0
    computer_cards= [get_card()]
    computer_final_score = 0
    for key in computer_cards:
        computer_final_score+=key
    for key in user_cards:
            total_user_score +=key

    print(f"Your cards: {user_cards}, current score: {total_user_score}")
    print(f"Computer's first card: {computer_cards}")
    game_on = True
    while game_on:
        pass_stay = input("Type 'y' to get another card, type 'n' to pass: ")
        if pass_stay == "y":
            next_card = get_card()
            user_cards.append(next_card)
            total_user_score+=next_card
            print(f"Your cards: {user_cards}, current score: {total_user_score}")
            print(f"Computer's first card: {computer_cards}")
            if total_user_score > 21:
                for number in user_cards:
                    if number == 11:
                        total_user_score -= 10


                if total_user_score > 21:
                    print("You lose, You went over board")
                    print(f"Your final hand is: {user_cards}, "
                          f"final score: {total_user_score} ")
                    print(f"Computer final hand is: {computer_cards}, "
                          f"final score: {computer_final_score} ")
                    game_on = False
                elif total_user_score == 21:
                    print("Blackjack, You win")
                    print(f"Your final hand is: {user_cards}, "
                          f"final score: {total_user_score} ")
                    print(f"Computer final hand is: {computer_cards}, "
                          f"final score: {computer_final_score} ")
                    game_on = False
        elif pass_stay == "n":
            print(f"Your final hand is: {user_cards}, "
                  f"final score: {total_user_score} ")

            while computer_final_score < 17:
                    computer_next_card = get_card()
                    computer_cards.append(computer_next_card)
                    computer_final_score+=computer_next_card
                    if computer_final_score > 21 and 11 in computer_cards:
                        computer_cards[computer_cards.index(11)] = 1
                        computer_final_score = sum(computer_cards)

            print(f"Computer final hand: "
                              f"{computer_cards}, final score: "
                              f"{computer_final_score}")

            if computer_final_score > 21:
                print("You win, Computer went over board")
                game_on = False

            elif computer_final_score == 21:
                print("Computer gets blackjack, Computer wins")
                game_on = False

            elif total_user_score > computer_final_score:
                print("You win")
                game_on = False

            elif total_user_score < computer_final_score:
                print("Computer wins")
                game_on = False

            elif total_user_score == computer_final_score:
                print("Draw")
                game_on = False
game = True
while game:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == "y":
        black_jack()
    else:
        game = False
