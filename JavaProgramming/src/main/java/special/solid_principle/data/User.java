package special.solid_principle.data;

import java.util.ArrayList;

public class User {
    private int id;
    private String name;
    private Address address;
    private ArrayList<Seller> sellers;

    public User(int id, String name, ArrayList<Seller> sellers) {
        this.id = id;
        this.name = name;
        this.sellers = sellers;
    }

    public User(int id, String name, Address address) {
        this.id = id;
        this.name = name;
        this.address = address;
    }

    public String getName() {
        return name;
    }

    public ArrayList<Seller> getSellers() {
        return sellers;
    }

    public Address getAddress() {
        return address;
    }
}
