def mergeSort(array):
    if len(array) == 1:
        return array
    else:
        midPoint = len(array) // 2  # Get the middle point of the array

        # Split array in two
        leftArray = array[:midPoint]  # Array elements BEFORE midPoint
        rightArray = array[midPoint:]  # Array elements AFTER midPoint

        print(f"leftArray: {leftArray} || rightArray: {rightArray}")
        return merge(mergeSort(leftArray), mergeSort(rightArray))  # Break array down to pieces and then bring them back together in order


def merge(leftArray, rightArray):
    # Get number of elements in leftArray and rightArray
    leftArrayLength = len(leftArray)
    rightArrayLength = len(rightArray)

    leftArrayIndex = 0  # Marker to track location in leftArray
    rightArrayIndex = 0  # Marker to track location in rightArray

    sortedArray = []  # Array to hold the sorted elements from leftArray and rightArray
    # Sorted array will go from smallest to largest

    while leftArrayIndex < leftArrayLength and rightArrayIndex < rightArrayLength:  # While loop that goes through the elements of both leftArray and rightArray
        if leftArray[leftArrayIndex] < rightArray[rightArrayIndex]:  # If something from leftArray is SMALLER than something from rightArray
            sortedArray.append(leftArray[leftArrayIndex])  # Put the item from leftArray into sortedArray
            leftArrayIndex += 1  # Move up on the leftArray
        else:  # leftArray[leftArrayIndex] > rightArray[rightArrayIndex] # If something from rightArray is SMALLER than something from leftArray
            sortedArray.append(rightArray[rightArrayIndex])
            rightArrayIndex += 1  # Move up on the rightArray

    print(f"Sorted Array: {sortedArray} || LeftArray: {leftArray[leftArrayIndex:]} || RightArray: {rightArray[rightArrayIndex:]}")
    return sortedArray + leftArray[leftArrayIndex:] + rightArray[rightArrayIndex:]  # Returns only TWO filled arrays at a time

array = [5, 9, 3, 10, 45, 2, 0]
print(f"Array before merge sort: {array}")
print(mergeSort(array))


