package com.youtube.live._02;

// Object class: People
class People {
    private String name; // Encapsulation
    String domisili;
    String profesi;

    // constructor with parameter
    People(String name) {
        System.out.println("Call People "+name);
    }

    // constructor without parameter
    People() {
        System.out.println("Call People");
    }

    // Setter
    public void setName(String name) {
        this.name = name;
    }

    // Getter
    public String getName() {
        return name;
    }

}

class Developer extends People {
    int id;
    String institute;

    // constructor without parameter
    Developer() {
        System.out.println("Call Developer");
    }
}

class RobotFeatures implements Robot {

    @Override
    public void isTalk() {

    }

    @Override
    public boolean isWalk() {
        return true;
    }

    @Override
    public void isNewest() {

    }
}

class AIFeatures implements Robot {

    @Override
    public void isTalk() {

    }

    @Override
    public boolean isWalk() {
        return false;
    }

    @Override
    public void isNewest() {

    }
}

public class OOP_Program {
    public static void main(String[] args) {
        // Define class object 'People'
        People people = new People();
        people.setName("Kelvin");
        String name = people.getName();
        System.out.println(name);

        System.out.println();
        Developer developer = new Developer();
        developer.id = 1234;
        developer.setName("Andy");
        System.out.println(developer.id);
        System.out.println(developer.getName());

        RobotFeatures robotFeatures = new RobotFeatures();
        boolean robotWalk = robotFeatures.isWalk();
        System.out.println(robotWalk);

        AIFeatures aiFeatures = new AIFeatures();
        boolean aiWalk = aiFeatures.isWalk();
        System.out.println(aiWalk);

    }
}
