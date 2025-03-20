package material.m07;

// Class Object & Attribute
class People {
    private String name;
    String domisili;
    String profesi;

    private int x1, x2, x3, x4, x5, x6, x7, x8, x9, x10;

    public int getX1() {
        return x1;
    }

    public void setX1(int x1) {
        this.x1 = x1;
    }

    public int getX2() {
        return x2;
    }

    public void setX2(int x2) {
        this.x2 = x2;
    }

    public int getX3() {
        return x3;
    }

    public void setX3(int x3) {
        this.x3 = x3;
    }

    public int getX4() {
        return x4;
    }

    public void setX4(int x4) {
        this.x4 = x4;
    }

    public int getX5() {
        return x5;
    }

    public void setX5(int x5) {
        this.x5 = x5;
    }

    public int getX6() {
        return x6;
    }

    public void setX6(int x6) {
        this.x6 = x6;
    }

    public int getX7() {
        return x7;
    }

    public void setX7(int x7) {
        this.x7 = x7;
    }

    public int getX8() {
        return x8;
    }

    public void setX8(int x8) {
        this.x8 = x8;
    }

    public int getX9() {
        return x9;
    }

    public void setX9(int x9) {
        this.x9 = x9;
    }

    public int getX10() {
        return x10;
    }

    public void setX10(int x10) {
        this.x10 = x10;
    }

    // constructor without parameter
    People() {
        System.out.println("Call People");
    }
    // constructor with parameter
    People(String message) {
        System.out.println("Message: "+ message);
    }

    // Setter Name
    public void setName(String name) {
        this.name = name;
    }
    // Getter Name
    public String getName() {
        return name;
    }

}

public class OOP_People {
    public static void main(String[] args) {
        // Define class 'People'
        People people = new People();
        people.setName("Kelvin");
        String name = people.getName();
        System.out.println(name);
    }
}
