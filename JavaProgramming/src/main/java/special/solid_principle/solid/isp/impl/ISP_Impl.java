package special.solid_principle.solid.isp.impl;

public class ISP_Impl {
    public static void main(String[] args) {
        System.out.println("Car ISP");
        Car_ISP carIsp = new Car_ISP();
        carIsp.start();
        carIsp.stop();
        carIsp.drive();
        carIsp.opendoor();

        System.out.println("Plane ISP");
        Plane_ISP planeIsp = new Plane_ISP();
        planeIsp.start();
        planeIsp.stop();
        planeIsp.fly();
        planeIsp.takeoff();

        System.out.println("Ship ISP");
        Ship_ISP shipIsp = new Ship_ISP();
        shipIsp.start();
        shipIsp.stop();
        shipIsp.sail();
    }
}
