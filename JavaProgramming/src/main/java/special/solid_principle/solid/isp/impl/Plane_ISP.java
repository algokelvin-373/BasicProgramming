package special.solid_principle.solid.isp.impl;

public class Plane_ISP implements Transport_ISP, Plane_Transport_ISP {
    @Override
    public void start() {
        System.out.println("Implement Start");
    }

    @Override
    public void stop() {
        System.out.println("Implement Stop");
    }

    @Override
    public void fly() {
        System.out.println("Implement Fly");
    }

    @Override
    public void takeoff() {
        System.out.println("Implement TakeOff");
    }

}
