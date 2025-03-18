package javacase.Statistic;

public class MeanProgram {

    public static void main(String[] args) {
        Statistic statistic = new Statistic();

        String data = "5, 6, 3, 5, 3, 5, 4, 5, 7, 8, 5, 5";
        int[] dtNum = statistic.getDataNumber(data);

        System.out.println("Data : " + data);
        System.out.println("n    : " + dtNum.length);
        System.out.println("Mean : " + statistic.mean(dtNum));

    }

}
