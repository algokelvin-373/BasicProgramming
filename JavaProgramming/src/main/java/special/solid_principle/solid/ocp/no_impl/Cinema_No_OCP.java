package special.solid_principle.solid.ocp.no_impl;

public class Cinema_No_OCP {
    public Double price;
}

class StandardCinema_No_OCP extends Cinema_No_OCP {
    public StandardCinema_No_OCP(double price) {
        this.price = price;
    }
}

class DeluxeCinema_No_OCP extends Cinema_No_OCP {
    public DeluxeCinema_No_OCP(double price) {
        this.price = price;
    }
}

class PremiumCinema_No_OCP extends Cinema_No_OCP {
    public PremiumCinema_No_OCP(double price) {
        this.price = price;
    }
}
