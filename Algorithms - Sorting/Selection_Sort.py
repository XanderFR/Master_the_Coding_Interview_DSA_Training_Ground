def selectionSortOne(array):
    for index in range(len(array)):  # For loop goes from left to right
        # index = 0
        leftIndex = index
        # leftIndex = 0
        for rightIndex in range(index + 1, len(array)):  # Minus a left portion of array, for loop goes from left to right
            # rightIndex = 1
            # [2, 0]
            #  0, 1
            if array[rightIndex] < array[leftIndex]:  # If a number on the right side of the array is smaller than the left side
                # [2, 0]
                #  0, 1
                leftIndex = rightIndex  # leftIndex becomes rightIndex
                # leftIndex = 1
        # array[0], array[1] = array[1], array[0]
        # array[0], array[1] = 0, 2
        array[index], array[leftIndex] = array[leftIndex], array[index]  # Switch the elements


def selectionSortTwo(array):
    for index in range(len(array)):  # For loop goes from left to right
        # index = 0
        leftIndex = index
        # leftIndex = 0
        for rightIndex in range(index + 1, len(array)):  # Minus a left portion of array, for loop goes from left to right
            # rightIndex = 1
            # [2, 0]
            #  0, 1
            if array[rightIndex] < array[leftIndex]:  # If a number on the right side of the array is smaller than the left side
                # [2, 0]
                #  0, 1

                # array[0], array[1] = array[1], array[0]
                # array[0], array[1] = 0, 2
                array[leftIndex], array[rightIndex] = array[rightIndex], array[leftIndex]  # Switch the elements


def selectionSortThree(array):
    for leftIndex in range(len(array)):  # For loop goes from left to right
        # leftIndex = 0
        for rightIndex in range(leftIndex + 1, len(array)):  # Minus a left portion of array, for loop goes from left to right
            # rightIndex = 1
            # [2, 0]
            #  0, 1
            if array[rightIndex] < array[leftIndex]:  # If a number on the right side of the array is smaller than the left side
                # [2, 0]
                #  0, 1

                # array[0], array[1] = array[1], array[0]
                # array[0], array[1] = 0, 2
                array[leftIndex], array[rightIndex] = array[rightIndex], array[leftIndex]  # Switch the elements

arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
selectionSortOne(arr)
print(f"SelectionSort1: {arr}")

arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
selectionSortTwo(arr)
print(f"SelectionSort2: {arr}")

arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
selectionSortThree(arr)
print(f"SelectionSort3: {arr}")

