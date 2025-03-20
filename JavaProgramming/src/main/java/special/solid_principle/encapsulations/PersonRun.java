package special.solid_principle.encapsulations;

public class PersonRun {
    public static void main(String[] args) {
        Person person = new Person();
        person.setName("AlgoKelvin");
        // System.out.println(person.name); // Error: 'name' is private
        System.out.println(person.getName());
    }
}
