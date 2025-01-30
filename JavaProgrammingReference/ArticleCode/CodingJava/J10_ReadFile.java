import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class J10_ReadFile {
    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("FileText.txt");
        Scanner reader = new Scanner(file);
        while (reader.hasNextLine()) {
            System.out.println(reader.nextLine());
        }
    }
}
