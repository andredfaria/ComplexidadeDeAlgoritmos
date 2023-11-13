#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void quickSort(int arr[], int low, int high);

int partition(int arr[], int low, int high);

double measureTime(int arr[], int n)
{
    clock_t start, end;
    start = clock();
    quickSort(arr, 0, n - 1);
    end = clock();
    return ((double)(end - start)) / CLOCKS_PER_SEC;
}

void quickSort(int arr[], int low, int high)
{
    if (low < high)
    {
        int pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int partition(int arr[], int low, int high)
{
    int pivot = arr[high];
    int i = (low - 1);

    for (int j = low; j <= high - 1; j++)
    {
        if (arr[j] < pivot)
        {
            i++;
            // swap arr[i] and arr[j]
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    // swap arr[i + 1] and arr[high] (pivot)
    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;
    return (i + 1);
}

int main()
{
    int listSizes[] = {/*... Your list sizes ...*/};
    int numSizes = sizeof(listSizes) / sizeof(listSizes[0]);

    double executionTimes[numSizes];

    for (int i = 0; i < numSizes; i++)
    {
        int size = listSizes[i];
        int *arr = (int *)malloc(size * sizeof(int));

        for (int j = 0; j < size; j++)
        {
            arr[j] = rand() % 10000;
        }

        double timeTaken = measureTime(arr, size);
        executionTimes[i] = timeTaken;
        free(arr);
    }

    FILE *gnuplotPipe = popen("gnuplot -persistent", "w");
    fprintf(gnuplotPipe, "set title 'Desempenho do Quick Sort'\n");
    fprintf(gnuplotPipe, "set xlabel 'Tamanho da Lista'\n");
    fprintf(gnuplotPipe, "set ylabel 'Tempo de Execução (segundos)'\n");
    fprintf(gnuplotPipe, "plot '-' with linespoints title 'Tempo de Execução'\n");

    for (int i = 0; i < numSizes; i++)
    {
        fprintf(gnuplotPipe, "%d %f\n", listSizes[i], executionTimes[i]);
    }
    fprintf(gnuplotPipe, "e\n");

    pclose(gnuplotPipe);

    return 0;
}
