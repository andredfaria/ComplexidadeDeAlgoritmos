import time
import random
import matplotlib.pyplot as plt

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp)
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp)
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_value = max(arr)
    exp = 1
    while max_value // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Função para medir o tempo
def measure_time(arr):
    start_time = time.time()
    radix_sort(arr)
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
plt.title('Desempenho do Radix Sort')
plt.grid(True)
plt.show()
