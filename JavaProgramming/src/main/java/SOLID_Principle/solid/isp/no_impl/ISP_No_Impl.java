package SOLID_Principle.solid.isp.no_impl;

public class ISP_No_Impl {
    public static void main(String[] args) {
        System.out.println("Car No ISP");
        Car_No_ISP carNoIsp = new Car_No_ISP();
        carNoIsp.start();
        carNoIsp.stop();
        carNoIsp.drive();
        carNoIsp.opendoor();
        carNoIsp.fly();
        carNoIsp.takeoff();
        carNoIsp.sail();

        System.out.println("Plane No ISP");
        Plane_No_ISP planeNoIsp = new Plane_No_ISP();
        planeNoIsp.start();
        planeNoIsp.stop();
        planeNoIsp.drive();
        planeNoIsp.opendoor();
        planeNoIsp.fly();
        planeNoIsp.takeoff();
        planeNoIsp.sail();

        System.out.println("Ship No ISP");
        Ship_No_ISP shipNoIsp = new Ship_No_ISP();
        shipNoIsp.start();
        shipNoIsp.stop();
        shipNoIsp.drive();
        shipNoIsp.opendoor();
        shipNoIsp.fly();
        shipNoIsp.takeoff();
        shipNoIsp.sail();
    }
}
