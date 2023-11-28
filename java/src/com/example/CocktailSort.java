package com.example;
import java.util.Arrays;
import java.util.Random;

public class CocktailSort {
    public static void cocktailSort(int[] arr) {
        int n = arr.length;
        boolean swapped = true;
        int start = 0;
        int end = n - 1;

        while (swapped) {
            swapped = false;

            // Move o maior elemento para a direita
            for (int i = start; i < end; ++i) {
                if (arr[i] > arr[i + 1]) {
                    int temp = arr[i];
                    arr[i] = arr[i + 1];
                    arr[i + 1] = temp;
                    swapped = true;
                }
            }

            if (!swapped) {
                break;
            }

            swapped = false;
            end = end - 1;

            // Move o menor elemento para a esquerda
            for (int i = end - 1; i >= start; --i) {
                if (arr[i] > arr[i + 1]) {
                    int temp = arr[i];
                    arr[i] = arr[i + 1];
                    arr[i + 1] = temp;
                    swapped = true;
                }
            }

            start = start + 1;
        }
    }

    public static double measureTime(int[] arr) {
        long startTime = System.nanoTime();
        cocktailSort(arr);
        long endTime = System.nanoTime();
        return (endTime - startTime) / 1e9; // convertendo para segundos
    }

    public static void main(String[] args) {
        int[] listSizes = {100, 500, 1000, 2000, 5000};
        double[] executionTimes = new double[listSizes.length];

        for (int i = 0; i < listSizes.length; ++i) {
            int size = listSizes[i];
            int[] arr = new int[size];
            Random rand = new Random();

            for (int j = 0; j < size; ++j) {
                arr[j] = rand.nextInt(10000) + 1;
            }

            double timeTaken = measureTime(arr);
            executionTimes[i] = timeTaken;
        }

        // Imprimir os resultados
        System.out.println("Tamanho da Lista | Tempo de Execução (segundos)");
        System.out.println("------------------------------------------------");

        for (int i = 0; i < listSizes.length; ++i) {
            System.out.printf("%-16d %.6f%n", listSizes[i], executionTimes[i]);
        }
    }
}
