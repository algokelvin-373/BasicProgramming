package special.solid_principle.solid.dip.impl;

public class Motorcycle_DIP {
    private final EngineInterface engine;

    public Motorcycle_DIP(EngineInterface engine) {
        this.engine = engine;
    }

    void start() {
        engine.start();
    }
}
