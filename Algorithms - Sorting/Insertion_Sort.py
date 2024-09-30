def insertionSort(array):
    for index in range(1, len(array)):  # For loop goes from 1 to end
        print(f"Index = {index}")
        print(f"BEFORE WHILE LOOP: {array}")
        # print(f"while {index} > 0 and {array[index - 1]} > {array[index]}")
        while index > 0 and array[index - 1] > array[index]:  # While loop that brings smaller numbers to the left side of the array

            print(f"while index={index} > 0 and array[index - 1]={array[index - 1]} > array[index]={array[index]}")
            print(f"Switching {array[index]} with {array[index - 1]}")

            array[index], array[index - 1] = array[index - 1], array[index]  # Switch values
            index -= 1  # Decrease the index | Helps bring the smaller numbers to the left side of the array

        print(f"AFTER WHILE LOOP:  {array}")
        print()

array = [3, 6, 1, 9, 2]
print(f"Array before sorting: {array}")
print()
insertionSort(array)
print(f"Array after sorting: {array}")
print()
array = [12, 11, 13, 5, 6]
print(f"Array before sorting: {array}")
insertionSort(array)
print(f"Array after sorting: {array}")

