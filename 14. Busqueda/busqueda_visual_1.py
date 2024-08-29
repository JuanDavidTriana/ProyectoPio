import matplotlib.pyplot as plt
import numpy as np

# Funciones de búsqueda
def busqueda_lineal(arr, x, draw_bars):
    for i in range(len(arr)):
        if arr[i] == x:
            draw_bars(arr, i, f'Linear Search - Elemento {x} encontrado en posición {i}')
            return i
        draw_bars(arr, i, f'Linear Search - Comparando posición {i}')
    return -1

def busqueda_binaria(arr, x, draw_bars):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        draw_bars(arr, mid, f'Binary Search - Comparando con posición {mid}')
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            draw_bars(arr, mid, f'Binary Search - Elemento {x} encontrado en posición {mid}')
            return mid
    return -1

# Función para visualizar el proceso de búsqueda
def draw_bars(arr, highlighted_idx, title):
    plt.cla()
    colors = ['blue'] * len(arr)
    if highlighted_idx is not None:
        colors[highlighted_idx] = 'red'
    plt.bar(range(len(arr)), arr, color=colors)
    plt.title(title)
    plt.pause(0.5)  # Tiempo de pausa para ver cada paso de la búsqueda

def main():
    # Crear una lista de números ordenados
    np.random.seed(0)
    arr = np.sort(np.random.randint(1, 1000, 100))  # Lista ordenada de 100 elementos
    x = int(input("Ingresa el número que deseas buscar: "))

    plt.figure(figsize=(15, 8))  # Tamaño de la figura ajustado para mayor cantidad de barras

    print("Elige el método de búsqueda:")
    print("1. Búsqueda Lineal")
    print("2. Búsqueda Binaria")
    choice = int(input("Ingresa el número de tu elección: "))

    if choice == 1:
        resultado = busqueda_lineal(arr, x, draw_bars)
        if resultado == -1:
            print(f"El elemento {x} no se encuentra en la lista.")
    elif choice == 2:
        resultado = busqueda_binaria(arr, x, draw_bars)
        if resultado == -1:
            print(f"El elemento {x} no se encuentra en la lista.")
    else:
        print("Opción no válida")

    plt.show()

if __name__ == "__main__":
    main()
