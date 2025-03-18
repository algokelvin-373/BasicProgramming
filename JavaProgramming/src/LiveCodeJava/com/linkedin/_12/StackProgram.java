package com.linkedin._12;

public class StackProgram {
    public static void main(String[] args) {
        // Sample Data Array Integer
        Integer[] data = {10, 25, 15, 70, 45};

        // Call 'stack' class
        Stack stack = new Stack(data.length);

        // 'Push'
        System.out.println("Program Push");
        for (Integer datum : data) {
            stack.push(datum);
        }
        for (Integer datum: stack.getStack()) {
            System.out.print(datum+"-");
        }
        System.out.println();

        // 'Pop'
        System.out.println("Program Pop");
        for (Integer datum : data) {
            stack.pop();
        }
        for (Integer datum: stack.getStack()) {
            System.out.print(datum+"-");
        }

    }
}

class Stack {
    private final Integer[] stack;
    private int size = 0;
    public Stack(int size) {
        this.stack = new Integer[size];
    }
    public void push(int data) {
        if (full()) System.out.println("Full data");
        else stack[size++] = data;
    }
    public void pop() {
        if (empty()) System.out.println("Empty data");
        else stack[--size] = null;
    }
    public Integer[] getStack() {
        return stack;
    }
    private boolean empty() {
        return size == 0;
    }
    private boolean full() {
        return size == stack.length;
    }
}
