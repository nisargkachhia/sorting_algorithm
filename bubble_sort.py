import random

def bubble_sort(arr):
    n = len(arr)
    # Perform n-1 passes over the array
    for i in range(n):
        # Initialize a flag to detect if any swaps occurred in this pass
        swapped = False
        
        # Iterate through the array, comparing adjacent elements
        for j in range(0, n - i - 1):
            # If the current element is greater than the next, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # A swap has occurred, so mark swapped as True
        
        # If no swaps occurred in the entire pass, the array is already sorted
        if not swapped:
            break
    return arr

# Generate a list of 5 random integers between 0 and 100
numbers = [random.randint(0, 100) for _ in range(5)]
print("Unsorted Array:", numbers)
# Sort the array using bubble sort
sorted_numbers = bubble_sort(numbers)
print("Sorted Array:", sorted_numbers)
