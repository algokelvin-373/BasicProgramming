package SOLID_Principle.solid.ocp.impl;

abstract class Cinema_OCP {
    double price;
    abstract double calculateAdminFee();
}

class StandardCinema_OCP extends Cinema_OCP {
    public StandardCinema_OCP(double price) {
        this.price = price;
    }

    @Override
    double calculateAdminFee() {
        return price * 10 / 100;
    }
}

class PremiumCinema_OCP extends Cinema_OCP {
    public PremiumCinema_OCP(double price) {
        this.price = price;
    }

    @Override
    double calculateAdminFee() {
        return price * 20 / 100;
    }
}

class DeluxeCinema_OCP extends Cinema_OCP {
    public DeluxeCinema_OCP(double price) {
        this.price = price;
    }

    @Override
    double calculateAdminFee() {
        return price * 12 / 100;
    }
}
