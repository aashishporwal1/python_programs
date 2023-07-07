import numpy as np

# Create an unsorted NumPy array
arr = np.array([5, 2, 8, 1, 6])

# Selection sort implementation
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Sort the array
selection_sort(arr)

# Print the sorted array
print(arr)

