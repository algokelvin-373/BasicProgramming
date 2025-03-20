package special.solid_principle.solid.dip.impl;

public class DIP_Impl {
    public static void main(String[] args) {
        Motorcycle_DIP motorcycleEngine = new Motorcycle_DIP(new Engine_DIP());
        Motorcycle_DIP motorcycleDieselEngine = new Motorcycle_DIP(new DieselEngine_DIP());
        Motorcycle_DIP motorcycleHybridEngine = new Motorcycle_DIP(new HybridEngine_DIP());

        motorcycleEngine.start();
        motorcycleDieselEngine.start();
        motorcycleHybridEngine.start();
    }
}
