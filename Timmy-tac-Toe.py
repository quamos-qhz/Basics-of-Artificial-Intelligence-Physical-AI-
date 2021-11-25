# Copyright <2019> <Kern Fowler, Sirajus Salekin, H M QUAMRAN HASAN @ KAIST>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
# Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# Import declarations
import random
import modi
import time


turnNumber = 0

# MODI Declarations
bundle = modi.MODI()
# led = bundle.leds[0]
motor_x = bundle.motors[0]
motor_y = bundle.motors[1]
motor_pen = bundle.motors[2]
# display = bundle.displays[0]

# CODE


def getDifficulty():
    difficulty = ''
    while not (difficulty == '1' or difficulty == '2' or difficulty == '3' or difficulty == '4'):
        print ("Please enter a difficulty level: 1, 2, 3 or 4")
        difficulty = input()
    return difficulty


def drawboard(board):
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])


def getLetter():  # Get players input letter, void
        return ['X', 'O']


def whoGoesFirst():  # Get who goes first, void
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def playAgain():  # Play again? Void
    playAgain = ''
    print ("Do you want to play again? Y or N")
    while not (playAgain == 'Y' or playAgain == 'N'):
        playAgain = input().upper()
    if playAgain == 'Y':
        return True
    else:
        return False


def computerDraw():
    print('Draw0')
    motor_pen.second_torque(-100)
    time.sleep(0.5)
    motor_pen.second_torque(0)
    motor_pen.first_torque(100)
    time.sleep(2)
    motor_pen.first_torque(0)
    motor_pen.second_torque(100)
    time.sleep(0.5)
    motor_pen.second_torque(0)


def position1():
    print('pos1')
    motor_x.speed(100, -100)
    time.sleep(3)
    motor_x.speed(0, 0)
    motor_y.speed(100, -100)
    time.sleep(3)
    motor_y.speed(0, 0)
    computerDraw()
    motor_y.speed(-100, 100)
    time.sleep(3)
    motor_y.speed(0, 0)
    motor_x.speed(-100, 100)
    time.sleep(3)
    motor_x.speed(0, 0)


def position2():
    print('pos2')
    motor_x.speed(100, -100)
    time.sleep(2)
    motor_x.speed(0, 0)
    motor_y.speed(100, -100)
    time.sleep(2)
    motor_y.speed(0, 0)
    computerDraw()
    motor_y.speed(-100, 100)
    time.sleep(2)
    motor_x.speed(0, 0)
    motor_x.speed(-100, 100)
    time.sleep(2)
    motor_y.speed(0, 0)


def position3():
    print('pos3')
    motor_x.speed(100, -100)
    time.sleep(2)
    motor_x.speed(0, 0)
    motor_y.speed(100, -100)
    time.sleep(2)
    motor_y.speed(0, 0)
    computerDraw()
    motor_y.speed(-100, 100)
    time.sleep(2)
    motor_x.speed(0, 0)
    motor_x.speed(-100, 100)
    time.sleep(2)
    motor_y.speed(0, 0)


def position4():
    print('pos4')
    motor_x.speed(100, -100)
    time.sleep(2)
    motor_x.speed(0, 0)
    motor_y.speed(100, -100)
    time.sleep(2)
    motor_y.speed(0, 0)
    computerDraw()
    motor_y.speed(-100, 100)
    time.sleep(2)
    motor_x.speed(0, 0)
    motor_x.speed(-100, 100)
    time.sleep(2)
    motor_y.speed(0, 0)


def position5():
    print('pos5')
    motor_x.speed(100, -100)
    time.sleep(2)
    motor_x.speed(0, 0)
    motor_y.speed(100, -100)
    time.sleep(2)
    motor_y.speed(0, 0)
    computerDraw()
    motor_y.speed(-100, 100)
    time.sleep(2)
    motor_x.speed(0, 0)
    motor_x.speed(-100, 100)
    time.sleep(2)
    motor_y.speed(0, 0)


def position6():
    print('pos6')
    motor_x.speed(100, -100)
    time.sleep(2)
    motor_x.speed(0, 0)
    motor_y.speed(100, -100)
    time.sleep(2)
    motor_y.speed(0, 0)
    computerDraw()
    motor_y.speed(-100, 100)
    time.sleep(2)
    motor_x.speed(0, 0)
    motor_x.speed(-100, 100)
    time.sleep(2)
    motor_y.speed(0, 0)


def position7():
    print('pos7')
    motor_x.speed(100, -100)
    time.sleep(2)
    motor_x.speed(0, 0)
    motor_y.speed(100, -100)
    time.sleep(2)
    motor_y.speed(0, 0)
    computerDraw()
    motor_y.speed(-100, 100)
    time.sleep(2)
    motor_x.speed(0, 0)
    motor_x.speed(-100, 100)
    time.sleep(2)
    motor_y.speed(0, 0)


def position8():
    print('pos8')
    motor_x.speed(100, -100)
    time.sleep(2)
    motor_x.speed(0, 0)
    motor_y.speed(100, -100)
    time.sleep(2)
    motor_y.speed(0, 0)
    computerDraw()
    motor_y.speed(-100, 100)
    time.sleep(2)
    motor_x.speed(0, 0)
    motor_x.speed(-100, 100)
    time.sleep(2)
    motor_y.speed(0, 0)


def position9():
    print ('pos9')
    motor_x.speed(100, -100)
    time.sleep(2)
    motor_x.speed(0, 0)
    motor_y.speed(100, -100)
    time.sleep(2)
    motor_y.speed(0, 0)
    computerDraw()
    motor_y.speed(-100, 100)
    time.sleep(2)
    motor_x.speed(0, 0)
    motor_x.speed(-100, 100)
    time.sleep(2)
    motor_y.speed(0, 0)


def computerMove(move):
    if move == 1:
        position1()
    if move == 2:
        position2()
    if move == 3:
        position3()
    if move == 4:
        position4()
    if move == 5:
        position5()
    if move == 6:
        position6()
    if move == 7:
        position7()
    if move == 8:
        position8()
    if move == 9:
        position9()


def makeMove(board, letter, move):  # Make move taking argument board letter and move
    if isSpaceFree(board, move):
        board[move] = letter


def isWinner(bo, le):  # Is winner taking argument board and letter
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal


def getBoardCopy(board):  # Get a copy of the board, taking argument board
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard


def isSpaceFree(board, move):  # Is space free, taking argument board and move
    if board[move] == ' ':
        return True
    else:
        return False


def getPlayerMove(board):  # Get player move, taking argument board
    print ("Choose a place to put your letter. Remember the board goes: 7, 8, 9. 4, 5, 6. 1, 2, 3")
    move = 0
    while not (move > 0 and move < 10) or not isSpaceFree(board, move):
        move = int(input())
    return move


def getRandomMove(board, moves):  # Choose random move from list taking argument board and list of moves
    possibleMoves = []
    for i in moves:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def getExpertMove(board, computerletter, theFirstPlayer, turnNumber):  # Get A.I move, taking argument board and computerletter
    if computerletter == 'X':
        playersLetter = 'O'
    else:
        playersLetter = 'X'

    for i in range(1, 10):  # Check for each place in the board
        copy = getBoardCopy(board)
        makeMove(copy, computerletter, i)
        if isWinner(copy, computerletter):
            return i

    for i in range(1, 10):  # Check if player could win in next move, and block them
        copy = getBoardCopy(board)
        makeMove(copy, playersLetter, i)
        if isWinner(copy, playersLetter):
            return i

    if theFirstPlayer == 'player':
        if isSpaceFree(board, 5):
            return 5

    if turnNumber == 2 and theFirstPlayer == 'player':
        move = getRandomMove(board, [2, 4, 6, 8])
        if move != None:
            return move

    move = getRandomMove(board, [7, 9, 1, 3]) # Take one of the cornors is free, using the Choose random move from list function
    if move != None:
        return move

    if isSpaceFree(board, 5):  # Try to take the center if free
        return 5

    move = getRandomMove(board, [2, 4, 6, 8])  # Take on of the sides. Using the choose random move from list function
    if move != None:
        return move


def getBeginnerMove(board, computerletter):
    move = getRandomMove(board, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    if move != None:
        return move


def getEasyMove(board, computerletter):
    if computerletter == 'X':
        playersLetter = 'O'
    else:
        playersLetter = 'X'

    for i in range(1, 10):
        copy = getBoardCopy(board)
        makeMove(copy, computerletter, i)
        if isWinner(copy, computerletter):
            return i

    for i in range(1, 10):  # Check if player could win in next move, and block them
        copy = getBoardCopy(board)
        makeMove(copy, playersLetter, i)
        if isWinner(copy, playersLetter):
            return i

    move = getRandomMove(board, [1, 2,3,4,5,6,7,8,9])
    if move != None:
        return move


def getIntermediateMove(board, computerletter):
    if computerletter == 'X':
        playersLetter = 'O'
    else:
        playersLetter = 'X'

    for i in range(1, 10):
        copy = getBoardCopy(board)
        makeMove(copy, computerletter, i)
        if isWinner(copy, computerletter):
            return i

    for i in range(1, 10):  # Check if player could win in next move, and block them
        copy = getBoardCopy(board)
        makeMove(copy, playersLetter, i)
        if isWinner(copy, playersLetter):
            return i

    move = getRandomMove(board, [7, 9, 1, 3])
    if move != None:
        return move

    if isSpaceFree(board, 5):   # Try to take the center if free
        return 5

    move = getRandomMove(board, [2, 4, 6, 8])
    if move != None:
        return move


def getComputerMove(board, computerletter, theFirstPlayer, turnNumber, difficulty):
    if difficulty == '1':
        move = getEasyMove(board, computerletter)
        return move
    if difficulty == '2':
        move = getBeginnerMove(board, computerletter)
        return move
    if difficulty == '3':
        move = getIntermediateMove(board, computerletter)
        return move
    if difficulty == '4':
        move = getExpertMove(board, computerletter, theFirstPlayer, turnNumber)
        return move


def boardFull(board):  # Is board full, taking argument board
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


# Main


print ("Welcome to tic tac toe, let me tell you on before hand that you won't win...")
while True:
    motor_y.speed(0, 0)
    motor_x.speed(0, 0)
    motor_pen.speed(0, 0)
    difficulty = getDifficulty()
    board = [' '] * 10
    playersLetter, computerletter = getLetter()
    turn = whoGoesFirst()
    theFirstPlayer = turn
    if turn == 'player':
        print ("You go first")
    else:
        print ("The computer goes first")
    gameIsPlaying = True
    turnNumber = 0
    # led.on()

    while gameIsPlaying:
        if turn == 'player':
            # led.rgb(0, 255, 0)
            drawboard(board)
            move = getPlayerMove(board)
            makeMove(board, playersLetter, move)

            if isWinner(board, playersLetter):
                drawboard(board)
                print ("Wow you won! There must be a mistake in the A.I algorithm...")
                gameIsPlaying = False
            if boardFull(board):
                drawboard(board)
                print ("It is a tie!")
                gameIsPlaying = False
            else:
                turn = 'computer'

        else:
            turnNumber += 1
            # led.rgb(255, 0, 0)
            move = getComputerMove(board, computerletter, theFirstPlayer, turnNumber, difficulty)
            makeMove(board, computerletter, move)
            computerMove(move)

            if isWinner(board, computerletter):
                drawboard(board)
                print ("The computer won, no wonder uh?")
                gameIsPlaying = False
            if boardFull(board):
                drawboard(board)
                print ("It is a tie!")
                gameIsPlaying = False
            else:
                turn = 'player'

    if not playAgain():
        break