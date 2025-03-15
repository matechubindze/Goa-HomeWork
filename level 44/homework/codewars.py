#1
def countdown(n):
    if n > 0:
        return list(range(n, 0, -1))
    else:
        return []
    
n = 5
print(countdown(n))
#2
def rock_paper_scissors(players):
    player1, player2 = players
    if player1 == player2:
        return "Draw!"
    elif (player1 == "scissors" and player2 == "paper") or (player1 == "paper" and player2 == "rock") or (player1 == "rock" and player2 == "scissors"):
        return "Player 1 won!"
    else:
        return "Player 2 won!"
#3
def is_divisible(n, x, y):
    return n % x == 0 and n % y == 0
#4
def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1, n + 1))
#5
def get_grade(score1, score2, score3):
    average_score = (score1 + score2 + score3) / 3
    
    if 90 <= average_score <= 100:
        return 'A'
    elif 80 <= average_score < 90:
        return 'B'
    elif 70 <= average_score < 80:
        return 'C'
    elif 60 <= average_score < 70:
        return 'D'
    else:
        return 'F'
