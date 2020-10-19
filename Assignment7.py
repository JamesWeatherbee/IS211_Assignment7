import random


class Player:
    def __init__(self, name, score, turn, current_roll):
        self.name = name
        self.score = score
        self.turn = turn
        self.current_roll = current_roll


class Die:
    random.seed(0)

    def __init__(self, num_sides=6):
        self.num_sides = num_sides
        self.current_value = self.roll()

    def roll(self):
        self.current_value = random.randrange(1, self.num_sides+1)
        return self.current_value


running = True


def main():
    print('\tWELCOME TO PIG!')
    print('The first person to get 100 points wins!')
    print('\nPlayer 1 will roll the die first.')

    player1 = Player('Player 1', 0, True, 0)
    player2 = Player('Player 2', 0, False, 0)

    while running:
        print('*' * 50)
        print('\n\tSCOREBOARD:\nPlayer 1: {} Points\nPlayer 2: {} Points'.format(player1.score, player2.score))
        if player1.turn == True:
            my_die = Die()
            print('\nPlayer 1 rolled a {}.'.format(my_die.current_value))
            if my_die.current_value != 1:
                player1.current_roll = player1.current_roll + my_die.current_value
                print('\nPlayer 1, Current Turn: {}'.format(player1.current_roll))
                choice = input('Would you like to hold and pass the dice (h) or roll again (r)? ')
                if choice == 'h':
                    player1.score = player1.score + player1.current_roll
                    if player1.score >= 100:
                        print('Player 1 Wins with a score of {}!'.format(player1.score))
                        raise SystemExit
                    else:
                        print('You are keeping this rounds points.  Pass the die to Player 2.')
                        player1.current_roll = 0
                        player1.turn = False
                        player2.turn = True
                elif choice == 'r':
                    player1.turn = True
            elif my_die.current_value == 1: # Do what happens if the player rolls a 1.
                print('***Sorry, you have rolled a 1 and lose all points for this round.***')
                print('Pass the die to Player 2.')
                player1.current_roll = 1
                player1.turn = False
                player2.turn = True

        if player2.turn == True:
            my_die = Die()
            print('*' * 50)
            print('\nPlayer 2 rolled a {}.'.format(my_die.current_value))
            print('\n\tSCOREBOARD:\nPlayer 1: {} Points\nPlayer 2: {} Points'.format(player1.score, player2.score))
            if my_die.current_value != 1:
                player2.current_roll = player2.current_roll + my_die.current_value
                print('\nPlayer 2 Current Turn: {}'.format(player2.current_roll))
                choice = input('Would you like to hold and pass the dice (h) or roll again (r)? ')
                if choice == 'h':
                    player2.current_roll = player2.current_roll + my_die.current_value
                    player2.score = player2.score + player2.current_roll
                    if player2.score >= 100:
                        print('Player 2 Wins with a score of {}!'.format(player2.score))
                        raise SystemExit
                    else:
                        print('You are keeping this rounds points.  Pass the die to Player 1.')
                        player2.current_roll = 0
                        player2.turn = False
                        player1.turn = True
                elif choice == 'r':
                    player2.turn = True
            elif my_die.current_value == 1: # Do what happens if the player rolls a 1.
                print('***Sorry, you have rolled a 1 and lose all points for this round.***')
                print('Pass the die back to Player 1.')
                player2.current_roll = 0
                player2.turn = False
                player1.turn = True


if __name__ == '__main__':
    main()