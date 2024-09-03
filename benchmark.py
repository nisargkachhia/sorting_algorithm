import random
import timeit
import matplotlib.pyplot as plt
import platform
import psutil

# Import sorting functions
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from bubble_sort import bubble_sort

def benchmark_sort(sort_func, input_sizes):
    times = []

    for size in input_sizes:
        # Generate a random array of the given size
        arr = [random.randint(0, 10000) for _ in range(size)]
        
        # Measure the time it takes to sort the array using timeit
        time_taken = timeit.timeit(lambda: sort_func(arr.copy()), number=1)
        times.append(time_taken)
        print(f"{sort_func.__name__.replace('_', ' ').title()} - Input Size: {size}, Time Taken: {time_taken:.6f} seconds")
    
    return times

# Define input sizes
input_sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]

# Benchmark each sorting function
bubble_times = benchmark_sort(bubble_sort, input_sizes)
insertion_times = benchmark_sort(insertion_sort, input_sizes)
selection_times = benchmark_sort(selection_sort, input_sizes)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, bubble_times, marker='o', label='Bubble Sort')
plt.plot(input_sizes, insertion_times, marker='o', label='Insertion Sort')
plt.plot(input_sizes, selection_times, marker='o', label='Selection Sort')
plt.title('Sorting Algorithms Time Complexity')
plt.xlabel('Input Size (n)')
plt.ylabel('Time Taken (seconds)')
plt.grid(True)
plt.legend()
plt.show()

# Print system information
print("\nSystem Information:")
print(f"Platform: {platform.system()} {platform.release()}")
print(f"Processor: {platform.processor()}")
print(f"RAM: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB")
print(f"Python Version: {platform.python_version()}")
print(f"ROM: {psutil.disk_usage('/').total / (1024 ** 3):.2f} GB")