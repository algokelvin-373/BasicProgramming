package special.solid_principle.solid.isp.impl;

public class Car_ISP implements Transport_ISP, Car_Transport_ISP {
    @Override
    public void start() {
        System.out.println("Implement Start");
    }

    @Override
    public void stop() {
        System.out.println("Implement Stop");
    }

    @Override
    public void drive() {
        System.out.println("Implement Drive");
    }

    @Override
    public void opendoor() {
        System.out.println("Implement Open Door");
    }

}
