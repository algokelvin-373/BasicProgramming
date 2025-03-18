package com.linkedin._13;

public class QueueProgram {
    public static void main(String[] args) {
        String[] data = {"Java", "Kotlin", "Python", "Dart", "Javascript"};
        Queue queue = new Queue(data.length);

        // Enqueue
        for (String dt: data) queue.enqueue(dt);

        // Data queue
        System.out.print("Queue 1: ");
        for (String dt: queue.getData()) System.out.print(dt+"-");
        System.out.println();

        queue.dequeue(); // Dequeue 'Java'
        queue.dequeue(); // Dequeue 'Kotlin'
        System.out.print("Queue 2: ");
        for (String dt: queue.getData()) System.out.print(dt+"-");
        System.out.println();

        queue.enqueue("Swift"); // Enqueue 'Swift'
        queue.enqueue("Golang"); // Enqueue 'Golang'
        System.out.print("Queue 3: ");
        for (String dt: queue.getData()) System.out.print(dt+"-");
        System.out.println();
    }
}

class Queue {
    private final String[] data;
    private int size = 0;

    Queue(int size) {
        this.data = new String[size];
    }
    public String[] getData() { return data; }
    public void enqueue(String dt) {
        if (isFull()) { System.out.println("The queue is full"); }
        else { data[size++] = dt; }
    }
    public void dequeue() {
        if (isEmpty()) { System.out.println("The queue is empty"); }
        else { updateQueue(); }
    }
    private void updateQueue() {
        for (int index = 1; index < data.length; index++) data[index - 1] = data[index];
        data[--size] = null;
    }
    private boolean isFull() { return size == data.length; }
    private boolean isEmpty() { return size == 0; }
}
