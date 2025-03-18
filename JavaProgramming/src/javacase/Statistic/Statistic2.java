package javacase.Statistic;

import java.util.Arrays;

public class Statistic2 {
    private int[] dataNumber;
    private int[][] modus;

    public int modus() {
        modusData(replaceArrayStr());
        return getModus(dataNumber);
    }

    private String replaceArrayStr() {
        String arrayStr = Arrays.toString(dataNumber);
        String rplArray = arrayStr.replace(",", "")
                .replace("[", "")
                .replace("]", "")
                .replace(" ", "");
        return removeDuplicate(rplArray);
    }

    private String removeDuplicate(String data) {
        String str = "";
        for (int x = 0; x < data.length(); x++) {
            char charAtPosition = data.charAt(x);
            if (str.indexOf(charAtPosition) < 0)
                str += charAtPosition;
        }
        return str;
    }

    private void modusData(String str) {
        modus = new int[str.length()][2];
        for (int i = 0; i < str.length(); i++) {
            modus[i][0] = Integer.parseInt(String.valueOf(str.charAt(i)));
            modus[i][1] = 0;
        }
    }

    private int getModus(int[] dt) {
        setAmountData(dt);
        int n = 0, max = modus[n][1];
        for (int m = 0; m < modus.length; m++) {
            if (max < modus[m][1]) {
                max = modus[m][1];
                n = m;
            }
        }
        return getDataModus();
    }

    private void setAmountData(int[] dt) {
        for (int i : dt) {
            for (int z = 0; z < modus.length; z++) {
                if (modus[z][0] == i) {
                    modus[z][1]++;
                    break;
                }
            }
        }
    }

    private int getDataModus() {
        int n = 0, max = modus[n][1];
        for (int m = 0; m < modus.length; m++) {
            if (max < modus[m][1]) {
                max = modus[m][1];
                n = m;
            }
        }
        return modus[n][0];
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
