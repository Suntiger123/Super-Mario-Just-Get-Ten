import bases
import possible

def propagation(n, myList, myTuple, tupleList):
    # Get initial value we are looking for
    initialTuple = tupleList[0]
    lastTuple = tupleList[len(tupleList)-1]

    # Define directions
    tupleUp    = (myTuple[0]-1, myTuple[1])
    tupleLeft  = (myTuple[0], myTuple[1]-1)
    tupleDown  = (myTuple[0]+1, myTuple[1])
    tupleRight = (myTuple[0], myTuple[1]+1)

    # Checking if cell position is not already on tupleList
    # In this case, we go out of the recursive function
    for item in range(len(tupleList)):
        if len(tupleList) > 1:
            tupleItem = tupleList[item]
            
            if myTuple[0] == tupleItem[0] and myTuple[1] == tupleItem[1]:
                return

    # Checking if initial value we are looking for is not the same as the current cell
    # In this case, we go out of the recursive function
    if myList[initialTuple[0]][initialTuple[1]] != myList[myTuple[0]][myTuple[1]]:
        return
    
    # Append myTuple to tupleList
    tupleList.append(myTuple)

    # Because at initial recursion, we need tuple in tupleList,
    # myTuple is added twice in the list - we remove the doublon
    if myTuple[0] == lastTuple[0] and myTuple[1] == lastTuple[1]:
        tupleList.pop()

    # All tests has passed
    # we search cells with same values around
    if myTuple[0]-1 != -1:
        propagation(n, myList, tupleUp, tupleList)
    if myTuple[1]-1 != -1:
        propagation(n, myList, tupleLeft, tupleList)
    if myTuple[0]+1 != n:
        propagation(n, myList, tupleDown, tupleList)
    if myTuple[1]+1 != n:
        propagation(n, myList, tupleRight, tupleList)

    return tupleList

def modification(n, myList, tupleList):
    firstItem = tupleList[0]
    myList[firstItem[0]][firstItem[1]] =  myList[firstItem[0]][firstItem[1]] + 1

    for item in tupleList[1:]:
        myList[item[0]][item[1]] = 0

    return tupleList

def gravity(n, myList, proba):
    for i in range(len(myList)):
        for j in range(len(myList[i])):
                if myList[i][j] == 0:
                    position = i
                    while position > 0:
                        myList[position][j] = myList[position-1][j]
                        position = position - 1
                        
                    myList[0][j] = bases.realNumber(proba)
