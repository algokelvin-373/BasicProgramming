package SOLID_Principle.inheritance;

public class AnimalBuffaloRun extends Buffalo {
    public static void main(String[] args) {
        Buffalo buffalo = new Buffalo();
        buffalo.play();
        buffalo.isHerbivore();
        buffalo.walk();
    }
}
