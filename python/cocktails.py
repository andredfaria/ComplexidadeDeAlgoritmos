import time
import random
import matplotlib.pyplot as plt

def cocktail_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n-1

    while (swapped == True):
        swapped = False

        # Move o maior elemento para a direita
        for i in range(start, end):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if (swapped == False):
            break

        swapped = False
        end = end - 1

        # Move o menor elemento para a esquerda
        for i in range(end-1, start-1, -1):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        start = start + 1
# Função para medir o tempo
def measure_time(arr):
    start_time = time.time()
    cocktail_sort(arr)
    end_time = time.time()
    return end_time - start_time

# Lista de tamanhos de listas
list_sizes = [100, 500, 1000, 2000, 5000]

# Medir o tempo para cada tamanho da lista
execution_times = []
for size in list_sizes:
    arr = [random.randint(1, 10000) for _ in range(size)]
    time_taken = measure_time(arr)
    execution_times.append(time_taken)

# Criar o gráfico
plt.plot(list_sizes, execution_times, marker='o', linestyle='-', color='b')
plt.xlabel('Tamanho da Lista')
plt.ylabel('Tempo de Execução (segundos)')
plt.title('Desempenho do Cocktail Sort')
plt.grid(True)
plt.show()
