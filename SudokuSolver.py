
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
    print(spaces)

# Each square should be the first 3 letters with the first 3 numbers and so on labeled square 1, 2, 3.....
def initSquares():
    tot = 0
    NumCount = 0
    LetterCount = 0
    while tot < 9:
        squares[str(tot)] = []
        if count == 9:
            count = 0
        

initSpaces()

#def square():
    # Check square
# Collects all values present in a square



#def init():

