package javacase.Statistic;


public class ModusProgram {
    private static int[][] modus;

    public static void main(String[] args) {
        Statistic2 statistic = new Statistic2();
        String data = "5, 6, 3, 5, 3, 5, 4, 5, 7, 8, 5";

        statistic.getDataNumber(data);
        int modusValue = statistic.modus();
        System.out.println("Modus: "+modusValue);
    }


}
