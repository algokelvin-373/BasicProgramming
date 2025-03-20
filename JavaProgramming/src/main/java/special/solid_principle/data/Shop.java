package special.solid_principle.data;

public class Shop {
    private int id;
    private String name;
    private Seller seller;

    public Shop(int id, String name, Seller seller) {
        this.id = id;
        this.name = name;
        this.seller = seller;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public final Seller getSeller() {
        return seller;
    }

    public void setSeller(Seller seller) {
        this.seller = seller;
    }
}
