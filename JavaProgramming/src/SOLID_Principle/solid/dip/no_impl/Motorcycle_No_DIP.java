package SOLID_Principle.solid.dip.no_impl;

public class Motorcycle_No_DIP {
    private final Engine_No_DIP engine;

    public Motorcycle_No_DIP(Engine_No_DIP engine) {
        this.engine = engine;
    }

    void start() {
        engine.start();
    }
}
