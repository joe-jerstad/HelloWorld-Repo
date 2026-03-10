def find_winner(player1='Rock', player2='Rock'):
    p1_wins = [('Rock', 'Scissors'), ('Scissors', 'Paper'), ('Paper', 'Rock')]

    if player1 == player2:
        return "It's a tie!"
    else:
        if (player1, player2) in p1_wins:
            return 'Player 1 wins!'
        else:
            return 'Player 2 wins!'
        
print(find_winner('Rock', 'Paper'))
print(find_winner('Scissors', 'Paper'))
print(find_winner('Rock', 'Rock'))
print(find_winner('Rock'))
print(find_winner())
print(find_winner('Scissors'))
