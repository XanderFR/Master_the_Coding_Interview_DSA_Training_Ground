def binarySearch(array, lowIndex, highIndex, target):
    if highIndex >= lowIndex:

        midPointIndex = (highIndex + lowIndex) // 2  # Get the middle index of array

        if array[midPointIndex] == target:  # If middle element of array equal to target
            return midPointIndex

        elif array[midPointIndex] > target:  # If middle element of array LARGER than target
            return binarySearch(array, lowIndex, midPointIndex, target)  # Run binarySearch with LOWER/LEFT HALF of array

        else:  # array[midPointIndex] < target | If middle element of array SMALLER than target
            return binarySearch(array, midPointIndex, highIndex, target)  # Run binarySearch with HIGHER/RIGHT HALF of array
    else:
        return -1  # Return -1 if target element not in the array

array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 15

result = binarySearch(array, 0, len(array), target)

if result == -1:
    print("Target not present in array")
else:
    print(f"The index of {target} is {result}")
