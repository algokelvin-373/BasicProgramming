package special.solid_principle.solid.ocp.no_impl;

public class CinemaCalculations {
    public double calculateAdminFee(Cinema_No_OCP cinema) {
        if (cinema instanceof StandardCinema_No_OCP) {
            return ((StandardCinema_No_OCP) cinema).price * 10 / 100;
        } else if (cinema instanceof DeluxeCinema_No_OCP) {
            return ((DeluxeCinema_No_OCP) cinema).price * 12 / 100;
        } else if (cinema instanceof PremiumCinema_No_OCP) {
            return ((PremiumCinema_No_OCP) cinema).price * 20 / 100;
        } else
            return 0.0;
    }
}
