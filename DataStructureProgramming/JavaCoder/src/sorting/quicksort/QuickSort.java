package sorting.quicksort;

import java.util.Random;

public class QuickSort {
    private int[] array;
    private int length;

    public void sort(int[] inputArr) {
        if (inputArr == null || inputArr.length == 0) return;
        this.array = inputArr;
        length = inputArr.length;
        quickSort(0, length - 1);
    }

    private void quickSort(int lowerIndex, int higherIndex) {
        int i = lowerIndex;
        int j = higherIndex;
        int pivot = array[lowerIndex + (higherIndex - lowerIndex) / 2];
        while (i <= j) {
            while (array[i] < pivot) i++;
            while (array[j] > pivot) j--;
            if (i <= j) {
                exchangeNumbers(i, j);
                i++;
                j--;
            }
        }
        if (lowerIndex < j) quickSort(lowerIndex, j);
        if (i < higherIndex) quickSort(i, higherIndex);
    }

    private void exchangeNumbers(int i, int j) {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }

    public static void main(String[] a) {
        Random in = new Random();
        QuickSort sorter = new QuickSort();
        int k, n = 100;
        int[] input = new int[n];
        for (k = 0; k < n; k++) input[k] = in.nextInt(1000);
        sorter.sort(input);
        for (int i : input) System.out.println(i);
    }
}
