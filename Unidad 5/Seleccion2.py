import matplotlib.pyplot as plt
import numpy as np

def selection_sort_visual(arr):
    n = len(arr)
    fig, ax = plt.subplots()
    ax.set_title('Selection Sort')

    xticks = range(len(arr))
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
        ax.clear()
        ax.bar(xticks, [ord(char) for char in arr], color='blue')
        ax.set_xticks(xticks)
        ax.set_xticklabels(arr)
        plt.pause(0.5)

    ax.clear()
    ax.bar(xticks, [ord(char) for char in arr], color='green')
    ax.set_xticks(xticks)
    ax.set_xticklabels(arr)
    ax.set_title('Sorted')
    plt.show()

letras = ['f', 'e', 'd', 'b', 'c', 'a']
print("Lista original:", letras)
selection_sort_visual(letras)
print("Lista ordenada:", letras)


