def bubbleSort(array):
    # Outer loop to go through array n times
    for n in range(len(array) - 1, 0, -1):  # for loop that goes from right to left of array
        # Every loop iteration leaves the larger values on the right side of the array alone
        # Inner loop to compare adjacent elements
        for i in range(n):
            if array[i] > array[i + 1]:  # If a number in the array is larger than a number on its right side
                array[i], array[i + 1] = array[i + 1], array[i]  # Switch the numbers | Left becomes right and right becomes left

array = [39, 12, 18, 85, 72, 10, 2, 18]
print("Unsorted list is:")
print(array)

bubbleSort(array)

print("Sorted list is:")
print(array)
