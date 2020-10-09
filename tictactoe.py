from random import randint
import time

class Player:

    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

    def get_move(self):

        move = ''

        while move not in range(1, 11):

            move = input('{}, select a position (1-9): '.format(self.name))
            print('\n')

            if move not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                print('That is not a valid position. Please try again.')
                print('\n')
                continue
                
            move = int(move)
        
        return (move, self.marker)

class Board:
    
    def __init__(self):
        self.positions = [' ' for x in range(0, 10)]

    def display(self):
        print('\n')
        print('{}|{}|{}'.format(self.positions[1], self.positions[2], self.positions[3]))
        print('-----')
        print('{}|{}|{}'.format(self.positions[4], self.positions[5], self.positions[6]))
        print('-----')
        print('{}|{}|{}'.format(self.positions[7], self.positions[8], self.positions[9]))
        print('\n'*5)

    def place_move(self, position, marker):
        self.positions[position] = marker
        print('{} was placed at position {}'.format(marker, position))

    def validate_move(self, position):
        if self.positions[position] == ' ':
            return True
        else: 
            print('That position has already been played. Try again')
            return False

    def walkthrough(self):
        walkthrough_board = ['', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        print('Below is what the gameboard is going to look like, with each position numbered.')
        print('These numbers are going to be used to reference specific positions when I ask for your moves')
        print('\n')

        print('{}|{}|{}'.format(walkthrough_board[1], walkthrough_board[2], walkthrough_board[3]))
        print('-----')
        print('{}|{}|{}'.format(walkthrough_board[4], walkthrough_board[5], walkthrough_board[6]))
        print('-----')
        print('{}|{}|{}'.format(walkthrough_board[7], walkthrough_board[8], walkthrough_board[9]))

    def is_full(self):
        valid_positions = self.positions[1:]

        for position in valid_positions:
            if position == ' ':
                return False
            else:
                continue

        return True
            
class TicTacToe:

    def __init__(self):
        self.game_over = False
        self.play_again = False
        self.gameboard = Board()
        self.winner = None
        self.current_turn = None
        self.p1 = None
        self.p2 = None

    def determine_first_turn(self):

        random_num = randint(0, 100)

        if (100 - random_num) > abs(0 - random_num):
            self.current_turn = self.p1
        else:
            self.current_turn = self.p2

    def toggle_current_turn(self):
        if self.current_turn == self.p1:
            self.current_turn = self.p2
        else:
            self.current_turn = self.p1

    def player_turn(self):

        valid_move = False

        while valid_move == False:

            # Get player input
            position, marker = self.current_turn.get_move()
            
            # If move is valid, place on the board. If not, restart while loop.
            if self.gameboard.validate_move(position):
                valid_move = True
                self.gameboard.place_move(position, marker)
            else:
                continue

    def initialize_players(self):
        p1_name = input('Player 1, what should I call you? ')
        print('Thank you, {}'.format(p1_name))
        p2_name = input('Player 2, what about you? ')
        print('Thank you, {}'.format(p2_name))
        print('\n')

        p1_marker = ''
        p2_marker = ''

        while p1_marker.lower() != 'x' and p1_marker.lower() != 'o':

            p1_marker = input('{}, you are player 1 so you get to pick your marker (X or O): '.format(p1_name))

            if p1_marker.lower() != 'x' and p1_marker.lower() != 'o':
                print('That is not an option, please try again.')
                continue
            else:
                p1_marker = p1_marker.upper()

                if p1_marker.lower() == 'x':
                    p2_marker = 'O'
                else:
                    p2_marker = 'X'

        self.p1 = Player(p1_name, p1_marker)
        self.p2 = Player(p2_name, p2_marker)

    def initialize_game(self):

        if not self.play_again:
            print('Welcome to my implementation of Tic Tac Toe.')
            print('My name is Morgan and I will be your host, let\'s get started!')
            print('\n')

            time.sleep(2)

            self.initialize_players()

            print('Initializing game...')
            print('\n')

            time.sleep(2)

            print('Game created! Next I am going to walk you through the gameboard.')
            print('\n')
            self.gameboard.walkthrough()

            time.sleep(5)

            print('\n')
            print('Alright, that\'s enough talking. Let\'s play!')
            print('\n')
            
        time.sleep(1)
        self.determine_first_turn()
        time.sleep(2)

        print('Congrats {}, you get to go first!'.format(self.current_turn.name))
        print('\n')

    def check_for_winner(self):
        if self.gameboard.positions[1] == self.current_turn.marker and self.gameboard.positions[2] == self.current_turn.marker and self.gameboard.positions[3] == self.current_turn.marker:
            self.winner = self.current_turn
            self.game_over = True
            return True
        if self.gameboard.positions[4] == self.current_turn.marker and self.gameboard.positions[5] == self.current_turn.marker and self.gameboard.positions[6] == self.current_turn.marker:
            self.winner = self.current_turn
            self.game_over = True
            return True
        if self.gameboard.positions[7] == self.current_turn.marker and self.gameboard.positions[8] == self.current_turn.marker and self.gameboard.positions[9] == self.current_turn.marker:
            self.winner = self.current_turn
            self.game_over = True
            return True
        if self.gameboard.positions[1] == self.current_turn.marker and self.gameboard.positions[5] == self.current_turn.marker and self.gameboard.positions[9] == self.current_turn.marker:
            self.winner = self.current_turn
            self.game_over = True
            return True
        if self.gameboard.positions[3] == self.current_turn.marker and self.gameboard.positions[5] == self.current_turn.marker and self.gameboard.positions[7] == self.current_turn.marker:
            self.winner = self.current_turn
            self.game_over = True
            return True
        if self.gameboard.positions[1] == self.current_turn.marker and self.gameboard.positions[4] == self.current_turn.marker and self.gameboard.positions[7] == self.current_turn.marker:
            self.winner = self.current_turn
            self.game_over = True
            return True
        if self.gameboard.positions[2] == self.current_turn.marker and self.gameboard.positions[5] == self.current_turn.marker and self.gameboard.positions[8] == self.current_turn.marker:
            self.winner = self.current_turn
            self.game_over = True
            return True
        if self.gameboard.positions[3] == self.current_turn.marker and self.gameboard.positions[6] == self.current_turn.marker and self.gameboard.positions[9] == self.current_turn.marker:
            self.winner = self.current_turn
            self.game_over = True
            return True

        return False
        
    def congratulate_winner(self):
        self.gameboard.display()

        print('Congratulations, {}! You have won!!'.format(self.winner.name))

    def reset_game_for_play_again(self):
        self.game_over = False
        self.play_again = True
        self.gameboard = Board()
        self.winner = None
        self.current_turn = None

        self.determine_first_turn()

    def check_play_again(self):
        choice = ''

        while choice.lower() != 'y' and choice.lower() != 'n':

            choice = input('Would you like to play again? (y/n) ')

            if choice.lower() != 'y' and choice.lower() != 'n':
                print('Sorry, that is not a valid choice. Try again.')
                continue
            if choice.lower() == 'y':

                self.reset_game_for_play_again()

            if choice.lower() == 'n':
                print('Thank you for playing, have a nice day! :)')
                quit()

    def tie_message(self):
        print('Wow, it seems that the game is a tie! Good game!')

    def play_game(self):         
        ### GAME INTRODUCTION ###

        self.initialize_game()

        ### GAME ###

        while self.game_over == False:

            print('Let\'s check out what the board looks like!')
            time.sleep(1)
            self.gameboard.display()
            
            time.sleep(.5)

            self.player_turn()

            if self.check_for_winner():

                # Print a message congratulating the winner
                self.congratulate_winner()          

                # Check if the users would like to play again
                self.check_play_again()
            else:
                if self.gameboard.is_full():

                    # Print a message notifying users of a tie
                    self.tie_message()

                    # Check if users would like to play again
                    self.check_play_again()

                else:
                    self.toggle_current_turn()
                    continue

### START GAME ###

Game = TicTacToe()

Game.play_game()






