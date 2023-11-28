package com.example;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

public class QuickSortPerformance {

    public static List<Integer> quickSort(List<Integer> arr) {
        if (arr.size() <= 1) {
            return arr;
        } else {
            int pivot = arr.get(0);
            List<Integer> less = new ArrayList<>();
            List<Integer> greater = new ArrayList<>();
            for (int i = 1; i < arr.size(); i++) {
                if (arr.get(i) <= pivot) {
                    less.add(arr.get(i));
                } else {
                    greater.add(arr.get(i));
                }
            }
            List<Integer> sortedLess = quickSort(less);
            List<Integer> sortedGreater = quickSort(greater);
            List<Integer> result = new ArrayList<>(sortedLess);
            result.add(pivot);
            result.addAll(sortedGreater);
            return result;
        }
    }

    public static double measureTime(List<Integer> arr) {
        long startTime = System.currentTimeMillis();
        quickSort(arr);
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
