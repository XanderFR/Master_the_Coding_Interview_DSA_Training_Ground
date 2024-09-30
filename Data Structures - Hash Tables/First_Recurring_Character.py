def firstRecurringChar(array):
    numberDict = dict()  # For holding numbers and how many times they appear in array

    for number in array:
        if number not in numberDict:  # If number not registered in dictionary
            numberDict[number] = 1  # Mark the number's first appearance
        else:  # If number already in numberDict
            numberDict[number] += 1  # Set number's appearance count to 2
            print(numberDict)  # Print the current tally
            return number  # Return the number with most appearances and break loop

    return "Undefined"

array1 = [2, 5, 1, 2, 3, 5, 1, 2, 4]
array2 = [2, 1, 1, 2, 3, 5, 1, 2, 4]
array3 = [2, 3, 4, 5]
array4 = [2, 5, 5, 2, 3, 5, 1, 2, 4]

print(firstRecurringChar(array1))
print()
print(firstRecurringChar(array2))
print()
print(firstRecurringChar(array3))
print()
print(firstRecurringChar(array4))
