import random

#Author: Michael Blostein
#Welcome to my Tic Tac Toe game!


X_SYMBOL= 'X'
O_SYMBOL= 'O'


board=['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
test_board = ['#','X','O','X','O','X','O','X','O','X']


def first_row_board(board): #returns the first row of the board
    print(' '*3 + '|' + ' '*3 + '|' + ' '*3)
    print(' '+ board[7]+ ' ' +'|'+ ' ' + board[8]+ ' ' +'|'+ ' '+ board[9]+ ' ')
    print(' '*3 + '|' + ' '*3 + '|' + ' '*3)
    print('-' *11)


def middle_row_board(board): #returns the middle row of the board
    print(' '*3 + '|' + ' '*3 + '|' + ' '*3)
    print(' '+ board[4]+ ' ' +'|'+ ' ' + board[5]+ ' ' +'|'+ ' '+ board[6]+ ' ')
    print(' '*3 + '|' + ' '*3 + '|' + ' '*3)
    print('-' *11)


def last_row_board(board): #returns the last row of the board
    print(' '*3 + '|' + ' '*3 + '|' + ' '*3)
    print(' '+ board[1]+ ' ' +'|'+ ' ' + board[2]+ ' ' +'|'+ ' '+ board[3]+ ' ')
    print(' '*3 + '|' + ' '*3 + '|' + ' '*3)


def display_board(board):#displays the full board
    '''
    >>>display_board(['#','X','O','X','O','X','O','X','O','X'])
       |   |  
     X | O | X 
       |   |   
    -----------
       |   |   
     O | X | O 
       |   |   
    -----------
       |   |   
     X | O | X 
       |   |
    '''
    first_row_board(board)
    middle_row_board(board)
    last_row_board(board)


def player_input(): #takes in a player input and assign their marker as 'X' or 'O'.
    '''
    >>>player_input()
    Player 1, you get to choose the marker you will be playing with.
    Player 1: Do you want to be X or O: X
    ('X', 'O')
    '''
    print('Player 1, you get to choose the marker you will be playing with.')
    
    marker_player1='wrong'
    acceptable_values= [X_SYMBOL, O_SYMBOL]
    
    while marker_player1 not in acceptable_values:
        marker_player1= input('Player 1: Do you want to be X or O: ').upper()
        if marker_player1 == X_SYMBOL:
            return ('X', 'O')
        elif marker_player1 == O_SYMBOL:
            return ('O', 'X')
        else:
            print('You have entered a wrong input. Please enter X or O.')
            

def place_marker(board, marker, position): #returns the marker (either X or O) at position indicated by user in board
    '''
    >>>place_marker(test_board,'$',8)
       |   |   
     X | $ | X 
       |   |   
    -----------
       |   |   
     O | X | O 
       |   |   
    -----------
       |   |   
     X | O | X 
       |   |   
    '''
    board[position]=marker
    


def win_check(board, marker): #takes in a board and a marker (X or O) and indicates if marker won the game (returns bool)
    '''
    >>>win_check(test_board, 'X')
    True
    >>>win_check(test_board, 'O')
    False
    >>>win_check(board,'X')
    False
    '''
    if marker== X_SYMBOL:
        return (board[1:4] == ['X', 'X', 'X'] or board[4:7] == ['X', 'X', 'X']  or board[7:] == ['X', 'X', 'X'] or
        board[1:8:3]== ['X', 'X', 'X']  or board[2:9:3]==['X', 'X', 'X']  or board[3::3]==['X', 'X', 'X'] or
        board[1::4]==['X', 'X', 'X'] or board[3:8:2]==['X', 'X', 'X'])
    
        
    elif marker== O_SYMBOL:
        return (board[1:4] == ['O', 'O', 'O'] or board[4:7] == ['O', 'O', 'O'] or board[7:] == ['O', 'O', 'O'] or
        board[1:8:3]==['O', 'O', 'O'] or board[2:9:3]==['O', 'O', 'O'] or board[3::3]==['O', 'O', 'O'] or
        board[1::4]==['O', 'O', 'O'] or board[3:8:2]==['O', 'O', 'O'])
        

def who_goes_first(): #returns a string of which player goes first
    '''
    >>>who_goes_first()
    'Player 1'
    '''
    player1_number= random.randint(1,2)
    
    if player1_number == 1:
        return 'Player 1'
    else:
        return 'Player 2'
    

def space_check(board, position): #returns False if there is a marker at this position
    '''
    >>>space_check(test_board, 8)
    False
    >>>space_check(board, 2)
    True
    '''
    return (board[position]== ' ')


def full_board_check(board): #returns false if the board is not full of markers
    '''
    >>>full_board_check(board)
    False
    >>>full_board_check(test_board)
    True
    '''
    index=0
    while index<9:
        if board[index]== ' ':
            return False
        index+=1
        
    return True
        

def player_choice(board): #asks for a players next position and if its a free position, stores this position for later use
    '''
    >>>player_choice(board)
    
    '''
    position= 0
    
    while position not in [1,2,3, 4,5,6,7,8,9] or not space_check(board, position):
        position= int(input('Choose your next position(1-9): '))
     
        #while not space_check(board, position):
            #print('Invalid input. Please enter a position that has no marker already on it.')
    
        if position not in [1, 2, 3, 4, 5, 6, 7 ,8 ,9]:
           print('Invalid input. Please enter a position between 1 and 9.')
            
    return position
                

def replay(): #asks player if they want to replay and returns True if yes
    choice= 'wrong'
    acceptable_values= ['Yes', 'No', 'yes', 'no']
    
    while choice not in acceptable_values:
        choice= input('Do you want to replay (enter Yes or No)? ')
 
        if choice in acceptable_values:
            break
        else:
            print('Invalid input. Please enter Yes or No.')
            
    if choice== 'Yes' or choice== 'yes':
        return True
    else:
        return False
 

def tic_tac_toe_game(): #displays the whole game
    print("Welcome to Misha's tic tac toe game!")
    print('I hope you have fun!')
    
    while True:
        board= ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        
        player1_marker, player2_marker= player_input()
        turn= who_goes_first()
        print(turn, 'will go first.')
            
        ready= input(turn+', are you ready to play? (Enter Yes or No) ').lower()
            
        if ready== 'yes':
            game_on= True
        
            while game_on:
                if turn== 'Player 1':
                    display_board(board)
                    position= player_choice(board)
                    place_marker(board, player1_marker, position)
                    if win_check(board, player1_marker):
                        display_board(board)
                        print('Congrats player 1, you have won.')
                        game_on= False
                            
                    else:
                        if full_board_check(board):
                            display_board(board)
                            print('The game ends in a draw.')
                            game_on= False
                        else:
                            turn= 'Player 2'
                                
                else:
                    display_board(board)
                    position= player_choice(board)
                    place_marker(board, player2_marker, position)
                    if win_check(board, player2_marker):
                        display_board(board)
                        print('Congrats player 2, you have won.')
                        game_on= False
                            
                    else:
                        if full_board_check(board):
                            display_board(board)
                            print('The game ends in a draw.')
                            game_on= False
                        else:
                            turn= 'Player 1'
            
            if game_on== False:
                if replay()== True:
                    game_on= True
                else:
                    print('Thanks for playing. Hope you replay soon!')
                    break
            
        else:
            game_on=False
            print('Alright. Hope you play soon!')
            break
                
                
            
                            
                        
        

  