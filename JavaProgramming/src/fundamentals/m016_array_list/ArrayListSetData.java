import java.util.ArrayList;

public class ArrayListSetData {
    public static void main(String[] args) {
        ArrayList<Integer> dtNumber = new ArrayList<>();
        // Add Data 1, 2, 3, 4, 5
        dtNumber.add(1); dtNumber.add(2); dtNumber.add(3); dtNumber.add(4); dtNumber.add(5);

        dtNumber.set(2, 300); // Set Data for index 2 => 300
        dtNumber.set(4, 500); // Set Data for index 4 => 500

        // Get Data for index
        System.out.println("ArrayList data number: ");
        System.out.print(dtNumber.get(0)+" ");
        System.out.print(dtNumber.get(1)+" ");
        System.out.print(dtNumber.get(2)+" ");
        System.out.print(dtNumber.get(3)+" ");
        System.out.print(dtNumber.get(4)+" ");

    }
}
