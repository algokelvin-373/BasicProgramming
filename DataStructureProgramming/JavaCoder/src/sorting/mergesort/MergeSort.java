package sorting.mergesort;

import java.util.Random;

public class MergeSort {
    public static void main(String[] a) {
        int i, n=100;
        Random in = new Random();
        int[] array = new int[n];

        for (i = 0; i < n; i++) array[i] = in.nextInt(1000);

        mergeSort(array, 0, array.length - 1);
        for (i = 0; i < array.length; i++) System.out.println(array[i]);
    }

    public static void mergeSort(int[] array, int lo, int n) {
        int low = lo, high = n;
        if (low >= high) return;

        int middle = (low + high) / 2;
        mergeSort(array, low, middle);
        mergeSort(array, middle + 1, high);
        int end_low = middle;
        int start_high = middle + 1;
        while ((lo <= end_low) && (start_high <= high)) {
            if (array[low] < array[start_high]) low++;
            else {
                int Temp = array[start_high];
                for (int k = start_high - 1; k >= low; k--) array[k + 1] = array[k];
                array[low] = Temp;
                low++;
                end_low++;
                start_high++;
            }
        }
    }
}
