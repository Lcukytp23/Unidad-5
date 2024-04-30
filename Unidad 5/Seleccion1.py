import matplotlib.pyplot as plt
import numpy as np
import time

def selection_sort_visual(arr):
    n = len(arr)
    fig, ax = plt.subplots()
    ax.bar(range(len(arr)), arr, color='blue')
    ax.set_title('Selection Sort')
    plt.show(block=False)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        ax.clear()
        ax.bar(range(len(arr)), arr, color='blue')
        plt.pause(0.5)
    plt.close()
arr = np.random.randint(1, 100, size=10)
print("Lista original:", arr)
selection_sort_visual(arr)
print("Lista ordenada:", arr)
