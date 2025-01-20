import random

#player1 = [0,2,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,3,0,5,0,0,0,0,0,0,0,0,0,0,0]  # Number of pieces in each position at the start of the game (Player 1)
player1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0]
player2 = [0,2,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,3,0,5,0,0,0,0,0,0,0,0,0,0,0]  # Number of pieces in each position at the start of the game (Player 2)
DiceSwitch = False  # To control dice rolling
player1name = input("Player 1, please enter your name: ")
player2name = input("Player 2, please enter your name: ")

def show(DiceSwitch):  # To display the game board and dice numbers
    space = 40
    print("B    A   ", "-"*50, "  A    B")  # Display the top line of the board and position numbers for each player
    for i in range(1,13):   # Display each row of the board
        if i<4:             # Adjust spacing when both positions have two-digit numbers
            print(13-i, " ", 12+i, "  |_", chr(111)*player1[12+i],chr(174)*player2[13-i], " "*(space-(player1[12+i]+player2[13-i]+player1[13-i]+player2[12+i])),\
                  chr(111)*player1[13-i], chr(174)*B[12+i], "_|  ", 13-i, " ", 12+i)
        else:
            print(13-i, "  ", 12+i, "  |_", chr(111)*player1[12+i],chr(174)*player2[13-i], " "*(space-(player1[12+i]+player2[13-i]+player1[13-i]+player2[12+i])),\
                  chr(111)*player1[13-i], chr(174)*player2[12+i], "_|  ", 13-i, "  ", 12+i)
        if i == 6 :  # Display the middle line of the board
            if DiceSwitch :  # Whether to roll the dice or not
                if player1[0] > 0 or player2[0] > 0:  # Display captured pieces
                    print(" "*9,"-"*10," ", player1[0]*chr(111), " ","-"*(26-player1[0]-player2[0])," ", player2[0]*chr(174), " ", "-"*10, end=" ")
                else:
                    print(" "*9, "-" * 50, end=" ")
                print(" "*25, "->", random.randint(1, 6), "<-")  # Roll the dice
                DiceSwitch = False
            else:
                if player1[0] > 0 or player2[0] > 0:
                    print(" "*9,"-"*10," ", player1[0]*chr(111), " ","-"*(26-player1[0]-player2[0])," ", player2[0]*chr(174), " ", "-"*10)
                else:
                    print(" "*9, "-" * 50)
                DiceSwitch = True
    print(" "*9, "-"*50)  # Display the bottom line of the board
    #print(" ")
    SumPlayer1 = 0
    SumPlayer2 = 0
    for i in range(25,31):
        SumPlayer1 = SumPlayer1 + player1[i]
        SumPlayer2 = SumPlayer2 + player2[i]
    print(" "*9 ,SumPlayer1, ": ", chr(111), " "*36, chr(174), ": ", SumPlayer2 )
    return (DiceSwitch)

A = player1
B = player2
CurrentPlayer = "A"
DiceSwitch = show(DiceSwitch)
UserOrder = input("Press 't' to roll the dice or 'e' to exit the program: ")
while UserOrder == "t":  # Run the game as long as the dice are rolled
    DiceSwitch = show(DiceSwitch)
    if CurrentPlayer == "A":
        A = player1
        B = player2
        TPlayer1Name = player1name
        CurrentPlayer = "B"
    else:
        A = player2
        B = player1
        TPlayer1Name = player2name
        CurrentPlayer = "A"
    WrongMove = True   # Switch for an invalid move
    WrongMoveaPairing1 = True   # First switch for paired moves
    WrongMoveaPairing2 = True   # Second switch for paired moves
    while WrongMove:
        if WrongMoveaPairing1:
            num1 = int(input("{} Please enter your first move: ".format(TPlayer1Name)))
            num2 = int(input("{} Please enter your second move: ".format(TPlayer1Name)))
            jaygah_1 = int((num1 / 10))
            tas_1 = (num1 % 10)
            jaygah_2 = int((num2 / 10))
            tas_2 = (num2 % 10)

        if tas_1 == tas_2 and WrongMoveaPairing2:
            num3 = int(input("{} Please enter your third move: ".format(TPlayer1Name)))
            num4 = int(input("{} Please enter your fourth move: ".format(TPlayer1Name)))
            jaygah_3 = int((num3 / 10))
            tas_3 = (num3 % 10)
            jaygah_4 = int((num4 / 10))
            tas_4 = (num4 % 10)
        if (A[0] > 1 and jaygah_1 > 0) or (A[0] > 1 and jaygah_2 > 0):  # If more than one piece is out of the game
            print("* {} You must bring your captured pieces back into the game first *".format(TPlayer1Name))
            WrongMoveaPairing2 = True
        else:
            if A[0] == 1 and (jaygah_1 != 0 and jaygah_2 != 0):  # If only one piece is out of the game
                print("* {} You must bring your captured piece back into the game first *".format(TPlayer1Name))
                WrongMoveaPairing2 = True
            else:
                if A[jaygah_1] == 0:
                    print("* {} You do not have a piece to move in the first position. *".format(TPlayer1Name))
                    WrongMoveaPairing2 = True
                else:
                    if A[jaygah_2] == 0 and (jaygah_1 + tas_1) != jaygah_2:
                        print("* {} You do not have a piece to move in the second position. *".format(TPlayer1Name))
                        WrongMoveaPairing2 = True
                    else:
                        SumList = 0
                        for i in range(19):   # Check the first 19 positions for pieces to move
                            SumList = SumList + A[i]
                        if (jaygah_1 + tas_1 > 24 or jaygah_2 + tas_2 > 24) and SumList > 0:
                            print("* {} You cannot remove your pieces yet. *".format(TPlayer1Name))
                            WrongMoveaPairing2 = True
                        else:
                            if B[(25 - jaygah_1) - tas_1] > 1 or B[(25 - jaygah_2) - tas_2] > 1:
                                print("* {} The opponent has more than one piece in this position. *".format(TPlayer1Name))
                                WrongMoveaPairing2 = True
                            else:
                                if B[(25 - jaygah_1) - tas_1] == 1:  # Update the list when capturing an opponent's piece (Position 1)
                                    B[(25 - jaygah_1) - tas_1] = B[(25 - jaygah_1) - tas_1] - 1
                                    B[0] = B[0] + 1
                                if B[(25 - jaygah_2) - tas_2] == 1:  # Update the list when capturing an opponent's piece (Position 2)
                                    B[(25 - jaygah_2) - tas_2] = B[(25 - jaygah_2) - tas_2] - 1
                                    B[0] = B[0] + 1
                                A[jaygah_1] = A[jaygah_1] - 1  # Update the list when moving pieces
                                A[jaygah_1 + tas_1] = A[jaygah_1 + tas_1] + 1
                                A[jaygah_2] = A[jaygah_2] - 1
                                A[jaygah_2 + tas_2] = A[jaygah_2 + tas_2] + 1
                                if not WrongMoveaPairing1:
                                    WrongMoveaPairing2 = False
                                if tas_1 == tas_2 and WrongMoveaPairing1:
                                    jaygah_1 = jaygah_3
                                    tas_1 = tas_3
                                    jaygah_2 = jaygah_4
                                    tas_2 = tas_4
                                    WrongMoveaPairing1 = False
                                    WrongMoveaPairing2 = False
                                else:
                                    DiceSwitch = show(DiceSwitch)
                                    WrongMove = False
                                SumList = 0
                                for i in range(25):  # Check the first 25 positions for pieces to move
                                    SumList = SumList + A[i]
                                if SumList == 0:
                                    print("* {} Congratulations, you have won the game! *".format(TPlayer1Name))
                                    break

    UserOrder = input("Press 't' to roll the dice or 'e' to exit the program: ")