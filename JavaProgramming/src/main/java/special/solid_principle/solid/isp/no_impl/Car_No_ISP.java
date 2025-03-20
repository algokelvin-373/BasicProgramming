package special.solid_principle.solid.isp.no_impl;

public class Car_No_ISP implements Transport_No_ISP {
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

    // No Correct to implement this
    @Override
    public void fly() {
        System.out.println("Implement Fly");
    }

    // No Correct to implement this
    @Override
    public void takeoff() {
        System.out.println("Implement TakeOff");
    }

    // No Correct to implement this
    @Override
    public void sail() {
        System.out.println("Implement Sail");
    }
}
