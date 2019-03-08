
initList = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
allSquares = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
spaces = {}
squares = {}

def initSpaces():
    print("Enter number of spots to be filled: \n")
    num = input()
    print("Enter spaces to be filled: (Use: <spot> <value>)(Example: A4,2): \n")
    while num > 0:
        a = raw_input()
        b = a.split(',')
        spaces[b[0]] = []
        spaces[b[0]].append(b[1])
        # print(spaces)
        num -= 1
    LetterCount = 0
    NumCount = 0
    while LetterCount < 9:
        while NumCount < 9:
            partone = allSquares[LetterCount]
            parttwo = initList[NumCount]
            curr = partone + parttwo
            if curr not in spaces:
                spaces[curr] = initList
            NumCount += 1
        NumCount = 0
        LetterCount += 1
    # print(spaces)

# Each square should be the first 3 letters with the first 3 numbers and so on labeled square 1, 2, 3.....
def initSquares():
    tot = 1         # total squares
    breaker = 1     # breaks starts at 1
                        # if it hits 3 resets to 1
                        # Next set of squares: 6 resets to 4 and 9 resets to 7
    plusthree = 3   # Value of three to subtract from the breaker
    smallCount = 0  # Small count to get the asdf liek breaker
    letters = 0     # Letters list index
    numbers = 0     # Numbers list index

    while tot < 10:
        count = 0
        squares[str(tot)] = []
        while count < 9:
            break
        

initSpaces()

#def square():
    # Check square
# Collects all values present in a square



#def init():




def printBoard():
    print('[' + str(spaces['A1']) + str(spaces['A2']) + str(spaces['A3']) + '] [' + str(spaces['A4']) + str(spaces['A5']) + str(spaces['A6']) + '] [' + str(spaces['A7']) + str(spaces['A8']) + str(spaces['A9']) + '] \n')
    print('[' + str(spaces['B1']) + str(spaces['B2']) + str(spaces['B3']) + '] [' + str(spaces['B4']) + str(spaces['B5']) + str(spaces['B6']) + '] [' + str(spaces['B7']) + str(spaces['B8']) + str(spaces['B9']) + '] \n')
    print('[' + str(spaces['C1']) + str(spaces['C2']) + str(spaces['C3']) + '] [' + str(spaces['C4']) + str(spaces['C5']) + str(spaces['C6']) + '] [' + str(spaces['C7']) + str(spaces['C8']) + str(spaces['C9']) + '] \n')
    print('------------------------------------------------------------')
    print('[' + str(spaces['D1']) + str(spaces['D2']) + str(spaces['D3']) + '] [' + str(spaces['D4']) + str(spaces['D5']) + str(spaces['D6']) + '] [' + str(spaces['D7']) + str(spaces['D8']) + str(spaces['D9']) + '] \n')
    print('[' + str(spaces['E1']) + str(spaces['E2']) + str(spaces['E3']) + '] [' + str(spaces['E4']) + str(spaces['E5']) + str(spaces['E6']) + '] [' + str(spaces['E7']) + str(spaces['E8']) + str(spaces['E9']) + '] \n')
    print('[' + str(spaces['F1']) + str(spaces['F2']) + str(spaces['F3']) + '] [' + str(spaces['F4']) + str(spaces['F5']) + str(spaces['F6']) + '] [' + str(spaces['F7']) + str(spaces['F8']) + str(spaces['F9']) + '] \n')
    print('------------------------------------------------------------')
    print('[' + str(spaces['G1']) + str(spaces['G2']) + str(spaces['G3']) + '] [' + str(spaces['G4']) + str(spaces['G5']) + str(spaces['G6']) + '] [' + str(spaces['G7']) + str(spaces['G8']) + str(spaces['G9']) + '] \n')
    print('[' + str(spaces['H1']) + str(spaces['H2']) + str(spaces['H3']) + '] [' + str(spaces['H4']) + str(spaces['H5']) + str(spaces['H6']) + '] [' + str(spaces['H7']) + str(spaces['H8']) + str(spaces['H9']) + '] \n')
    print('[' + str(spaces['I1']) + str(spaces['I2']) + str(spaces['I3']) + '] [' + str(spaces['I4']) + str(spaces['I5']) + str(spaces['I6']) + '] [' + str(spaces['I7']) + str(spaces['I8']) + str(spaces['I9']) + '] \n')

printBoard()