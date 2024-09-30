def getCommonElements(firstArray, secondArray):  # O(n^2)

    # Compares every element in firstArray with every element in secondArray
    for element in firstArray:
        for item in secondArray:
            if element == item:
                return True
    return False


def smarterGetCommonElements(firstArray, secondArray):  # O(n+n)

    try:
        firstArrayDict = dict()  # Object to make comparisons easier

        # Turn firstArray into dictionary with unique elements from the array
        for element in firstArray:
            if element not in firstArrayDict:
                firstArrayDict[element] = True  # key: value => number: True

        for item in secondArray:  # Loop through secondArray elements
            if item in firstArrayDict:  # Ask firstArrayDict if it has a specific item
                return True

        return False

    except TypeError:
        return "Two arrays with similar contents required"


array1 = ['a', 'b', 'c', 'x', 'a']
array2 = ['z', 'y', 'i']

print(smarterGetCommonElements(array1, array2))

array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'x']

print(smarterGetCommonElements(array1, array2))




