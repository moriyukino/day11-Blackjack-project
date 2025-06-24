import random
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has Blackjack"
    elif u_score == 0:
        return  "Win with a Blackjack"
    elif u_score > 21:
        return "You went over. You lose"
    elif c_score > 21:
        return "Opponent went over. You win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _  in range(2):
    # 既存のリストにリストではなく、単一の項目だけを追加したい場合はappend( )を使用すること
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards},current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over =True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards},final score:{computer_score}")
    print(compare(user_score,computer_score))

while input("do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()


# def calculate_score():
#     total = sum(cards)
#     # エースの処理（最初は11としてカウント）
#     ace_count = cards.count(11)
#
#     # 合計が21を超えた場合、エースを1に変更
#     while total > 21 and ace_count:
#         total -= 10  # エースを11から1に変更
#         ace_count -= 1  # 1枚のエースを処理したのでカウントを減らす
#
#     return total
#
# def check_blackjack(cards):
#     if len(cards) == 2 and sum(cards) == 21:
#         return True
#     return False
#
# if check_blackjack(user_cards):
#     print("You have a Blackjack! 🎉 You win!")
# elif check_blackjack(computer_cards):
#     print("Computer has a Blackjack. 😱 You lose.")
# else:
#     print("No Blackjack this time. Let's continue!")
#
#
# user_score = calculate_score(user_cards)
#
# if user_score > 21:
#     print("You went over 21! 😢 You lose.")
# else:
#     if should_continue():
#         # 新しいカードを user_cards に追加
#         # そのあと、もう一度スコア計算して…（繰り返しもOK）
#
#
#
# def should_continue():
#     answer = input("Do you want to draw another card? (y/n): ").lower()
#     if answer == "y":
#         return True
#     else:
#         return False
#
#
#
# for random_card in range(0, 13):
#     user_cards.append(random.choice(card))
#
