package special.solid_principle.data;

public class Address {
    private int id;
    private String location;

    public Address(int id, String location) {
        this.id = id;
        this.location = location;
    }

    public String getLocation() {
        return location;
    }
}
