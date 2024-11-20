package sorting.shellsort;

import java.util.Random;

public class ShellSort {
    public static void main(String args[]) {
        int a, b, i, j, increment, temp, n=100;
        Random in = new Random();
        int[] array = new int[n];

        for(b=0;b<n;b++) array[b] = in.nextInt(1000);

        for (increment = array.length / 2; increment > 0; increment /= 2) {
            for (i = increment; i < array.length; i++) {
                temp = array[i];
                for (j = i; j >= increment; j -= increment) {
                    if (temp < array[j - increment]) array[j] = array[j - increment];
                    else break;
                }
                array[j] = temp;
            }
        }

        for (a = 0; a < array.length; a++) System.out.println(array[a]);
    }
}
