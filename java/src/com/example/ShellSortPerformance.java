package com.example;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

public class ShellSortPerformance {

    public static void shellSort(List<Integer> arr) {
        int n = arr.size();
        int gap = n / 2;
        while (gap > 0) {
            for (int i = gap; i < n; i++) {
                int temp = arr.get(i);
                int j = i;
                while (j >= gap && arr.get(j - gap) > temp) {
                    arr.set(j, arr.get(j - gap));
                    j -= gap;
                }
                arr.set(j, temp);
            }
            gap = gap / 2;
        }
    }

    public static double measureTime(List<Integer> arr) {
        long startTime = System.currentTimeMillis();
        shellSort(arr);
        long endTime = System.currentTimeMillis();
        return (endTime - startTime) / 1000.0; // Convert to seconds
    }

    public static void main(String[] args) {
        List<Integer> listSizes = Arrays.asList(
                100, 200, 300, 400, 500, 600, 700, 800, 900, 1000,
                // ... (remaining list sizes)
                19900, 20000
        );

        List<Double> executionTimes = new ArrayList<>();
        for (int size : listSizes) {
            List<Integer> arr = new ArrayList<>();
            Random random = new Random();
            for (int i = 0; i < size; i++) {
                arr.add(random.nextInt(10000) + 1);
            }
            double timeTaken = measureTime(arr);
            executionTimes.add(timeTaken);
        }

        // Print execution times
        for (int i = 0; i < listSizes.size(); i++) {
            System.out.println("Size: " + listSizes.get(i) + ", Time: " + executionTimes.get(i) + " seconds");
        }
    }
}
