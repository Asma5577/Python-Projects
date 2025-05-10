import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_initial_input = input("Do you want to play BlackJack? Type 'y' or 'n' :").lower()
if player_initial_input == "y":
    player_list=[]
    player_total_score=0
    for card in range(2):
        random_card = random.randint(0, 12)
        #player_random_cards = cards[random_card]
        player_list.append(cards[random_card])
        player_total_score += cards[random_card]

    print(f"Your cards: {player_list}, current score: {player_total_score}")
    random_card_com = random.randint(0, 12)
    com_list = []
    #com_first_card = cards[random_card_com]
    com_list.append(cards[random_card_com])
    print(f"Computer's first card: {cards[random_card_com]}")
    com_total = cards[random_card_com]


    input_another_card = input("Type 'y' to get another card and 'n' to pass: ").lower()

    if input_another_card == "y":
        another_random_card = random.randint(0, 12)
        player_list.append(cards[another_random_card])
        player_total_score += cards[another_random_card]
        print(f"Your cards: {player_list}, current score: {player_total_score}")

    else:
        while com_total < 16:
            rest_random_card_com = random.randint(0, 12)
            com_list.append(cards[rest_random_card_com])
            com_total += cards[rest_random_card_com]
        print(f"Compuer's Final hands {com_list} = {com_total}")

    if 21 > com_total > player_total_score:
        print("Computer is Winner")
    elif com_total == player_total_score and com_total<21:
        print("Draw the game")
    else:
        print("You win the game")














