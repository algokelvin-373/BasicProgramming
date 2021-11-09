package SOLID_Principle.solid.dip.no_impl;

public class DIP_No_Impl {
    public static void main(String[] args) {
        Engine_No_DIP engineNoDip = new Engine_No_DIP();
        Motorcycle_No_DIP motorcycleNoDip = new Motorcycle_No_DIP(engineNoDip);
        motorcycleNoDip.start();

        /* Error: Cannot be applied
        DieselEngine_No_DIP dieselEngineNoDip = new DieselEngine_No_DIP();
        Motorcycle_No_DIP motorcycleNoDip2 = new Motorcycle_No_DIP(dieselEngineNoDip);
         */

    }
}
