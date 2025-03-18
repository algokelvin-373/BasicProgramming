import java.util.ArrayList;

class Coding {
    private int id;
    private String name;

    public Coding(int id, String name) {
        this.id = id;
        this.name = name;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

}

class ListGeneric<T> {
    private ArrayList<T> data;

    public ListGeneric() {
        data = new ArrayList<T>();
    }

    public void addData(T dt) {
        data.add(dt);
    }

    public T getData(int index) {
        return data.get(index);
    }
}

public class J09_Generic {
    public static void main(String[] args) {
        ListGeneric<Coding> listGeneric = new ListGeneric<Coding>();

        listGeneric.addData(new Coding(1001, "Java"));
        Coding cd1 = listGeneric.getData(0);
        System.out.println(cd1.getId() + " - "+ cd1.getName());

        listGeneric.addData(new Coding(1002, "Python"));
        Coding cd2 = listGeneric.getData(1);
        System.out.println(cd2.getId() + " - "+ cd2.getName());
    }
}
