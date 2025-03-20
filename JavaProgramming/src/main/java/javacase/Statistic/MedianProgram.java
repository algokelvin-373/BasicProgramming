package javacase.Statistic;

public class MedianProgram {
    public static void main(String[] args) {
        Statistic statistic = new Statistic();

        // 3 3 4 5 5 [5] 5 5 6 7 8 - median
        String data = "5, 6, 5, 5, 3, 3, 4, 5, 7, 8, 5";
        int[] dtNum = statistic.getDataNumber(data);

        int length = dtNum.length;
        int median = dtNum[length/2];
        for (int x = 0; x < dtNum.length / 2; x++) {
            System.out.print("dt["+x+"] = "+dtNum[x]+" > "+median+" => ");
            if (dtNum[x] > median) {
                System.out.println("Masuk If");
                median = dtNum[x];
            }
        }
        System.out.println("Median sementara = " + median);
        for (int x = (dtNum.length / 2) + 1; x < dtNum.length; x++) {
            System.out.print("dt["+x+"] = "+dtNum[x]+" < "+median+" => ");
            if (dtNum[x] < median) {
                System.out.println("Masuk If");
                median = dtNum[x];
            }
        }
        System.out.println("Median akhir = " + median);

    }
}
