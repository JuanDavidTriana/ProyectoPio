import matplotlib.pyplot as plt
import numpy as np

# Funciones de ordenamiento
def bubble_sort(arr, draw_bars):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            draw_bars(arr, j, j+1, f'Bubble Sort - Iteración {i+1}, Comparando {arr[j]} y {arr[j+1]}')

def selection_sort(arr, draw_bars):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        draw_bars(arr, i, min_idx, f'Selection Sort - Colocando {arr[i]} en la posición {i+1}')

def insertion_sort(arr, draw_bars):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            draw_bars(arr, j + 1, i, f'Insertion Sort - Insertando {key} en la posición {j+1}')
        arr[j + 1] = key
        draw_bars(arr, j + 1, i, f'Insertion Sort - Insertando {key} en la posición {j+1}')

def quick_sort(arr, low, high, draw_bars):
    if low < high:
        pi = partition(arr, low, high, draw_bars)
        quick_sort(arr, low, pi-1, draw_bars)
        quick_sort(arr, pi+1, high, draw_bars)

def partition(arr, low, high, draw_bars):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
        draw_bars(arr, i, j, f'Quick Sort - Pivot {pivot}, Comparando {arr[j]}')
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    draw_bars(arr, i + 1, high, f'Quick Sort - Colocando Pivot {pivot} en la posición {i+1}')
    return i + 1

# Función para visualizar el proceso de ordenamiento
def draw_bars(arr, idx1, idx2, title):
    plt.cla()
    colors = ['blue'] * len(arr)
    if idx1 is not None:
        colors[idx1] = 'red'
    if idx2 is not None:
        colors[idx2] = 'green'
    plt.bar(range(len(arr)), arr, color=colors)
    plt.title(title)
    plt.xticks(range(len(arr)), arr, rotation=90, fontsize=8)
    plt.pause(0.1)  # Tiempo de pausa para ver cada paso del ordenamiento

def main():
    # Crear una lista del 1 al 100 en orden aleatorio
    arr = list(range(1, 100))
    np.random.shuffle(arr)
    
    plt.figure(figsize=(12, 6))  # Tamaño de la figura ajustado

    print("Elige el método de ordenamiento:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Quick Sort")
    choice = int(input("Ingresa el número de tu elección: "))

    if choice == 1:
        bubble_sort(arr, draw_bars)
    elif choice == 2:
        selection_sort(arr, draw_bars)
    elif choice == 3:
        insertion_sort(arr, draw_bars)
    elif choice == 4:
        quick_sort(arr, 0, len(arr)-1, draw_bars)
    else:
        print("Opción no válida")

    plt.show()

if __name__ == "__main__":
    main()
