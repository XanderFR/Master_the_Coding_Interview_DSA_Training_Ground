def linearSearch(array, target):
    for index in range(len(array)):  # For loop goes through all element of array
        if array[index] == target:  # If element at a given index is equal to target
            return index
    return -1  # Return -1 if target not found

array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 15

print(f"The index of {target} is {linearSearch(array, target)}")
