package com.linkedin._01;

class Message<T> {
    private T message;

    public void setMessage(T message) {
        this.message = message;
    }

    public T getMessage() {
        return message;
    }
}

public class GenericProgram {
    public static void main(String[] args) {
        // Generic 1, T = String
        Message<String> msg1 = new Message<>();
        msg1.setMessage("AlgoKelvin");

        // Generic 2, T = Integer
        Message<Integer> msg2 = new Message<>();
        msg2.setMessage(1000);

        System.out.println(msg1.getMessage()); // Generic 1
        System.out.println(msg2.getMessage()); // Generic 2
    }
}
