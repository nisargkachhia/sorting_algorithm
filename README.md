# DAA Hands On-2

## Argue Selection Sort Correctness

To demonstrate that the selection sort algorithm is correct, we need to establish three aspects of a loop invariant.

  - **Initialize**
  - **Maintenance**
  - **Termination** 

### 1. Initialization (Base Case):
Before the first iteration (i = 0), the subarray arr`[0:0]` is empty, which trivially satisfies the loop invariant. Hence, the loop invariant holds before the first iteration.

### 2. Maintenance (Inductive Step):
Assume that the loop invariant holds at the start of the `i`-th iteration. During this iteration, the algorithm selects the smallest element from the unsorted portion of the array `(arr[i:n])` and swaps it with the element at index `i`. After the swap, the subarray `arr[0:i+1]` will contain the smallest `i+1` elements in sorted order because:
The subarray `arr[0:i]` was already sorted by the induction hypothesis.
The newly placed element `arr[i]` is the smallest element from `arr[i:n]`, so the subarray `arr[0:i+1]` is sorted.
Thus, the loop invariant is maintained at the end of each iteration.

### 3. Termination (Final Case):
The algorithm terminates when `i = n`, at which point the entire array is sorted. Since the loop invariant holds at each iteration, by the time the loop finishes, the entire array `arr[0:n]` must be sorted.

## Benchmarking the Runtime of Each Algorithm

Your benchmarks should include information about your computer (RAM, CPU, etc.) and be run with various input sizes, from small (array of size 5, 10, 20) all the way up to large arrays (where your computer is struggling). Below is a plot of time vs input size `n`.

### System Information:
- **Platform:** Windows 10
- **Processor:** Intel64 Family 6 Model 142 Stepping 12, GenuineIntel
- **RAM:** 7.86 GB
- **Python Version:** 3.10.5
- **ROM:** 500.00 GB

### Benchmarks
- Bubble Sort - Input Size: 5, Time Taken: 0.000009 seconds
- Bubble Sort - Input Size: 10, Time Taken: 0.000013 seconds
- Bubble Sort - Input Size: 20, Time Taken: 0.000054 seconds
- Bubble Sort - Input Size: 50, Time Taken: 0.000229 seconds
- Bubble Sort - Input Size: 100, Time Taken: 0.000704 seconds
- Bubble Sort - Input Size: 200, Time Taken: 0.002599 seconds
- Bubble Sort - Input Size: 500, Time Taken: 0.036388 seconds
- Bubble Sort - Input Size: 1000, Time Taken: 0.095313 seconds
- Bubble Sort - Input Size: 2000, Time Taken: 0.371018 seconds
- Bubble Sort - Input Size: 5000, Time Taken: 3.903183 seconds
- Insertion Sort - Input Size: 5, Time Taken: 0.000011 seconds
- Insertion Sort - Input Size: 10, Time Taken: 0.000022 seconds
- Insertion Sort - Input Size: 20, Time Taken: 0.000033 seconds
- Insertion Sort - Input Size: 50, Time Taken: 0.000242 seconds
- Insertion Sort - Input Size: 100, Time Taken: 0.000717 seconds
- Insertion Sort - Input Size: 200, Time Taken: 0.006655 seconds
- Insertion Sort - Input Size: 500, Time Taken: 0.028255 seconds
- Insertion Sort - Input Size: 1000, Time Taken: 0.130120 seconds
- Insertion Sort - Input Size: 2000, Time Taken: 0.509646 seconds
- Insertion Sort - Input Size: 5000, Time Taken: 1.991360 seconds
- Selection Sort - Input Size: 5, Time Taken: 0.000009 seconds
- Selection Sort - Input Size: 10, Time Taken: 0.000012 seconds
- Selection Sort - Input Size: 20, Time Taken: 0.000025 seconds
- Selection Sort - Input Size: 50, Time Taken: 0.000204 seconds
- Selection Sort - Input Size: 100, Time Taken: 0.000502 seconds
- Selection Sort - Input Size: 200, Time Taken: 0.002287 seconds
- Selection Sort - Input Size: 500, Time Taken: 0.019244 seconds
- Selection Sort - Input Size: 1000, Time Taken: 0.071132 seconds
- Selection Sort - Input Size: 2000, Time Taken: 0.238462 seconds
- Selection Sort - Input Size: 5000, Time Taken: 1.049084 seconds


![Graph](https://github.com/user-attachments/assets/36da32fc-354f-4b8c-ac44-257d1758a445)
