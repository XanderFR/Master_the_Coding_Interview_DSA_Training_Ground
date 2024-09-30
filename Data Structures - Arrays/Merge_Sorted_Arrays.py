def mergeSortedArrays(array1, array2):
    # Check for empty arrays
    if len(array1) == 0:
        return array2
    if len(array2) == 0:
        return array1

    mergedArray = []  # The future home to the combined array elements

    # Markers to signal reaching the end of an array
    # The finish line
    finishLineOfFirstArray = len(array1)
    finishLineOfSecondArray = len(array2)

    # Markers that point to current location / index in an array
    # The racers slowly making their way to one of their respective finish lines
    firstArrayCurrentIndex = secondArrayCurrentIndex = 0  # Start at index 0 of first and second arrays

    # While the first racer is behind their finish line AND the second racer is behind their finish line
    # While loop only runs while both racers are behind their finish line
    # One racer index being the same number and the finishing line index breaks the loop
    while firstArrayCurrentIndex < finishLineOfFirstArray and secondArrayCurrentIndex < finishLineOfSecondArray:
        if array1[firstArrayCurrentIndex] <= array2[secondArrayCurrentIndex]:
            mergedArray.append(array1[firstArrayCurrentIndex])
            firstArrayCurrentIndex += 1
        else:
            mergedArray.append(array2[secondArrayCurrentIndex])
            secondArrayCurrentIndex += 1

    '''# Check useful variables
    print("current mergedArray: " + str(mergedArray))
    print("firstArrayCurrentIndex: " + str(firstArrayCurrentIndex))
    print("secondArrayCurrentIndex: " + str(secondArrayCurrentIndex))
    print("array1: " + str(array1[firstArrayCurrentIndex:]))
    print("array2: " + str(array2[secondArrayCurrentIndex:]))'''

    # Code block for adding the array1 or array2 leftovers to the mergedArray
    # Check which array leftovers is empty "[]"
    # If arrays are same length, this block shouldn't run because by then both arrays should be empty "[]"
    if len(array1[firstArrayCurrentIndex:]) > 0:
        for remainingElement in array1[firstArrayCurrentIndex:]:
            mergedArray.append(remainingElement)
    else:
        for remainingElement in array2[secondArrayCurrentIndex:]:
            mergedArray.append(remainingElement)

    return mergedArray


firstArray = [0, 3, 4, 31]
secondArray = [4, 6, 30]
print(mergeSortedArrays(firstArray, secondArray))

firstArray = [1, 3, 5, 7]
secondArray = [2, 4, 6, 8]
print(mergeSortedArrays(firstArray, secondArray))
