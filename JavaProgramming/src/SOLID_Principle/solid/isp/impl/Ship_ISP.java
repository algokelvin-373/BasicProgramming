package SOLID_Principle.solid.isp.impl;

public class Ship_ISP implements Transport_ISP, Ship_Transport_ISP {
    @Override
    public void start() {
        System.out.println("Implement Start");
    }

    @Override
    public void stop() {
        System.out.println("Implement Stop");
    }

    @Override
    public void sail() {
        System.out.println("Implement Sail");
    }
}
