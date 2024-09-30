def quickSort(array):
    # Example [0, 9, 3, 8, 2, 7, 5]
    length = len(array)  # 7
    if length <= 1:
        return array
    else:
        pivotPoint = array.pop()  # Remove last element of array and store in pivotPoint | 5

        # Example array is [0, 9, 3, 8, 2, 7]

    itemsGreater = []  # For numbers greater than pivotPoint
    itemsLower = []  # For numbers lower than pivotPoint

    for number in array:  # For loop to compare all numbers with pivotPoint
        if number > pivotPoint:
            itemsGreater.append(number)
        else:
            itemsLower.append(number)

    # After for loop one run
    # Less than pivot => [0, 3, 2] | more than pivot => [9, 8, 7]
    print(f"itemsLower: {itemsLower} + pivotPoint: {pivotPoint} + itemsGreater: {itemsGreater}")
    # Less than pivot => [0, 3, 2] | More than pivot => [9, 8, 7] get sent to same quickSort algorithm for further sorting
    # Apply quickSort algorithm to each sublist created
    return quickSort(itemsLower) + [pivotPoint] + quickSort(itemsGreater)

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(quickSort(numbers))
