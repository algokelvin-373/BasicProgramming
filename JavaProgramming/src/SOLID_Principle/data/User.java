package SOLID_Principle.data;

import java.util.ArrayList;

public class User {
    private int id;
    private String name;
    private ArrayList<Seller> sellers;

    public User(int id, String name, ArrayList<Seller> sellers) {
        this.id = id;
        this.name = name;
        this.sellers = sellers;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public ArrayList<Seller> getSellers() {
        return sellers;
    }
}
