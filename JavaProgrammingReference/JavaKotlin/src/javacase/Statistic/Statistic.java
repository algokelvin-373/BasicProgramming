package javacase.Statistic;

public class Statistic {
    private int[] dataNumber;
    private int sum = 0;

    public float mean(int[] dataNumber) {
        for (int dt: dataNumber) {
            sum += dt;
        }
        return (float) sum / dataNumber.length;
    }

    public int[] getDataNumber(String data) {
        String s = data.replace(" ", "");
        long countComa = s.chars().filter(c -> c == ',').count();
        dataNumber = new int[s.length() - (int) countComa];

        int y = 0;
        for (int x = 0; x < s.length(); x++) {
            if (s.charAt(x) == ',')
                setDataNumberArray(y++, s.charAt(x-1));
            if (x == s.length() - 1)
                setDataNumberArray(y, s.charAt(x));
        }
        return dataNumber;
    }

    private void setDataNumberArray(int i, char c) {
        dataNumber[i] = Integer.parseInt(String.valueOf(c));
    }
}
