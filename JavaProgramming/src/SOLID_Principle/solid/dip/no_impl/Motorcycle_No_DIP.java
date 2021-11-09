package SOLID_Principle.solid.dip.no_impl;

class Motorcycle_No_DIP {
    private Engine_No_DIP engine;
    private DieselEngine_No_DIP dieselEngine;

    Motorcycle_No_DIP(Engine_No_DIP engine) {
        this.engine = engine;
    }

    Motorcycle_No_DIP(DieselEngine_No_DIP dieselEngine) {
        this.dieselEngine = dieselEngine;
    }

    void start() {
        engine.start();
    }

    void startDiesel() {
        dieselEngine.start();
    }
}
