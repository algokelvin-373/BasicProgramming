import java.util.ArrayList;

public class LoopingForEachArrayList {
    public static void main(String[] args) {
        ArrayList<Integer> data = new ArrayList<>();
        data.add(1);
        data.add(2);
        data.add(3);
        data.add(4);
        data.add(5);

        for (int dt: data) {
            System.out.print(dt + " ");
        }
        System.out.println();
    }
}
