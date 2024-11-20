import java.util.ArrayList;

public class J08_ArrayList {
    public static void main(String[] args) {
        ArrayList<String> coding = new ArrayList<>();

        // Add data using ArrayList
        coding.add("Java");
        coding.add("Kotlin");
        coding.add("Python");

        // Show data list array
        for (int x = 0; x < coding.size(); x++) {
            System.out.println(coding.get(x));
        }
    }
}
