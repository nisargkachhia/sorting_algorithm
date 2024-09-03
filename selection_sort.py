import random

def selection_sort(arr):
    n = len(arr)
    
    # Traverse the entire array
    for i in range(n):
        # Start by assuming the first unsorted element as the minimum
        min_index = i
        # Look through the rest of the array to find the true minimum element
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # If the current element is not the smallest, swap it with the smallest element found
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
# Generate a list of 5 random integers between 0 and 100
numbers = [random.randint(0, 100) for _ in range(5)]
print("Unsorted Array:", numbers)
# Sort the array using selection sort
selection_sort(numbers)
print("Sorted Array:", numbers)