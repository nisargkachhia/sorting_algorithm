import random
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
# Generate a list of 5 random integers between 0 and 100
numbers = [random.randint(0, 100) for _ in range(5)]
print("Unsorted Array:", numbers)
# Sort the array using selection sort
insertion_sort(numbers)
print("Sorted Array:", numbers)