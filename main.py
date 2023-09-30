import random
count=0
total_matches=0
def update_high_score():
    '''This function simply updates the high score in the text file'''
    global high_score,saved_score
    if high_score>saved_score:
        with open("high_score.txt","w")as file:
            file.write(str(high_score))

def read_high_score():
    '''reads the text file in order to retrieve highest score. returns the saved highest score'''
    try:
        with open("high_score.txt","r")as file:
            saved_score=int(file.read())
    except FileNotFoundError:
        with open("high_score.txt","w") as file:
            file.write(str(0))
            saved_score=0
    return saved_score

def display_interface(board):
    '''prints out the interface'''
    print(f"{board[0]}\n{board[1]}\n{board[2]}\n")

def game_over(board):
    '''If conditions are met then end the match. increment score if player wins. In any case increment the matches played variable'''
    global high_score,total_matches
    if board[0][0]=="X" and board[0][1]=="X" and board[0][2]=="X":
        print("The player wins")
        total_matches+=1
        high_score+=1
        return False
    elif board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
        print("The computer wins")
        total_matches += 1

        return False
    elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
        print("The player wins")
        total_matches += 1
        high_score+=1
        return False
    elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
        print("The computer wins")
        total_matches += 1
        return False
    elif board[2][0]=="X" and board[2][1] == "X" and board[2][2] == "X":
        print("The player wins")
        total_matches += 1
        high_score += 1
        return False
    elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
        print("The computer wins")
        total_matches += 1

        return False
    elif board[0][0]=="X" and board[1][0]=="X" and board[2][0]=="X":
        print("The player wins")
        total_matches += 1
        high_score += 1
        return False
    elif board[0][0]=="O" and board[1][0]=="O" and board[2][0]=="O":
        print("The computer wins")
        total_matches += 1

        return False
    elif board[0][1]=="X" and board[1][1]=="X" and board[2][1]=="X":
        print("The player wins")
        total_matches += 1
        high_score += 1
        return False
    elif board[0][1]=="O" and board[1][1]=="O" and board[2][1]=="O":
        print("The computer wins")
        total_matches += 1

        return False
    elif board[0][2]=="X" and board[1][2]=="X" and board[2][2]=="X":
        print("The player wins")
        total_matches += 1
        high_score += 1
        return False
    elif board[0][2]=="O" and board[1][2]=="O" and board[2][2]=="O":
        print("The computer wins")
        total_matches += 1

        return False
    elif board[0][0]=="X" and board[1][1]=="X" and board[2][2]=="X":
        print("The player wins")
        total_matches += 1
        high_score += 1
        return False
    elif board[0][0]=="O" and board[1][1]=="O" and board[2][2]=="O":
        print("The computer wins")
        total_matches += 1

        return False
    elif board[0][2]=="X" and board[1][1]=="X" and board[2][0]=="X":
        print("The player wins")
        total_matches += 1
        high_score += 1
        return False
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        print("The computer wins")
        total_matches += 1
        return False
    else:
         return True

high_score=0
restart=True
player_indicator="X"
computer_indicator="O"
saved_score=read_high_score()
computer_moves=[]

while restart:
    board=[[" "," "," "],[" "," "," "],[" "," "," "]]



    update_high_score()
    game_is_on=True
    while game_is_on:
        #gets a user input as to where to place the player mark. the computers move is based on where the player moves
        #random.choice module is used in a list consisting of possible moves to block the users completion
        #after each round the computer moves list is cleared in order to keep the game going
        user_input=input("Where should i place your move?\nOptions are: 'top/middle/bottom' 'right/middle/left'\n").lower()
        if user_input=="top right" and board[0][2]==" ":
            board[0][2]=player_indicator
            computer_moves.append("top middle")
            computer_moves.append("middle right")
            computer_moves.append("middle middle")
        elif user_input=="top middle"and board[0][1]==" ":

            board[0][1]=player_indicator
            computer_moves.append("top left" )
            computer_moves.append("middle middle")

        elif user_input=="top left"and board[0][0]==" ":
            board[0][0]=player_indicator
            computer_moves.append("top middle")
            computer_moves.append("middle middle")
            computer_moves.append("middle left")
        elif user_input=="middle right"and board[1][2]==" ":
            board[1][2]=player_indicator
            computer_moves.append("top right")
            computer_moves.append("bottom right")
            computer_moves.append("middle middle")



        elif user_input == "middle middle"and board[1][1]==" ":
            board[1][1] = player_indicator
            computer_moves.append("top middle")
            computer_moves.append("middle right")
            computer_moves.append("middle left")
            computer_moves.append("top right")
        elif user_input=="middle left"and board[1][0]==" ":
            board[1][0]=player_indicator
            computer_moves.append("top left")
            computer_moves.append( "middle middle")
            computer_moves.append("bottom left")
        elif user_input=="bottom right"and board[2][2]==" ":
            board[2][2]=player_indicator
            computer_moves.append("middle right")
            computer_moves.append("bottom middle")

        elif user_input=="bottom middle"and board[2][1]==" ":
            board[2][1]=player_indicator
            computer_moves.append("bottom left")
            computer_moves.append("middle middle")
            computer_moves.append("middle left")

        elif user_input=="bottom left"and board[2][0]==" ":
            board[2][0]=player_indicator
            computer_moves.append("middle left")
            computer_moves.append("middle middle")
            computer_moves.append("top left")
        else:
            #if there already is something in the chosen cell break out of the loop
            print(f"{user_input.title()} is not an option or the spot has been taken. \nRestart Game")
            break
        #generates random computer move
        computer_move=random.choice(computer_moves)
        print(computer_move)
        #checks computer move if there is something in the cell. if there is generate another random computer move otherwise continue playing
        if computer_move=="top right" :
            if board[0][2] == " ":

                board[0][2]=computer_indicator
                computer_moves.clear()
            else:
                computer_move = random.choice(computer_moves)

        elif computer_move=="top middle":
            if board[0][1]==" ":
                board[0][1]=computer_indicator
                computer_moves.clear()

            else:
                computer_move = random.choice(computer_moves)

        elif computer_move=="top left":
            if board[0][0]==" ":
                board[0][0]=computer_indicator
                computer_moves.clear()

            else:
                computer_move = random.choice(computer_moves)

        elif computer_move=="middle right":
            if board[1][2]==" ":
                board[1][2]=computer_indicator
                computer_moves.clear()

            else:
                computer_move = random.choice(computer_moves)

        elif computer_move == "middle middle":
            if board[1][1]==" ":
                board[1][1] = computer_indicator
                computer_moves.clear()

            else:
                computer_move = random.choice(computer_moves)

        elif computer_move=="middle left":
            if board[1][0]==" ":
                board[1][0]=computer_indicator
                computer_moves.clear()

            else:
                computer_move = random.choice(computer_moves)

        elif computer_move=="bottom right":
            if board[2][2]==" ":
                board[2][2]=computer_indicator
                computer_moves.clear()

            else:
                computer_move = random.choice(computer_moves)

        elif computer_move=="bottom middle":
            if board[2][1]==" ":
                board[2][1]=computer_indicator
                computer_moves.clear()

            else:
                computer_move = random.choice(computer_moves)

        elif computer_move=="bottom left":
            if board[2][0]==" ":
                board[2][0]=computer_indicator
                computer_moves.clear()

            else:
                computer_move = random.choice(computer_moves)

        display_interface(board)
        game_is_on = game_over(board)
    print(f"Player has won {high_score}/{total_matches} matches played!!\n")

    update_high_score()
    play_again=input("Press 'm' to stop playing or anything else to keep playing\n").lower()
    if play_again=="n" or play_again=="no":
        restart=False



