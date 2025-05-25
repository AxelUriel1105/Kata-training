"""In this kata, your task is to implement an extended version of the famous rock-paper-scissors game. The rules are as follows:

Scissors cuts Paper
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock
Rock crushes Scissors
Task:
Given two values from the above game, return the Player result as "Player 1 Won!", "Player 2 Won!", or "Draw!"."""
def rpsls(pl1, pl2):
    print(pl1,pl2)
    if pl1 == pl2: return 'Draw!'
    counter_dict = {
        'Scissors': ('Paper','Lizard'),
        'Paper': ('Rock','Spock'),
        'Rock': ('Lizard', 'Scissors'),
        'Lizard': ('Spock','Paper'),
        'Spock': ('Scissors','Rock')
    }
    return 'Player 1 Won!' if pl2.title() in counter_dict.get(pl1.title()) else 'Player 2 Won!'
    