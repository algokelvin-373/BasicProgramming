package queue.dequeue;

public interface DequeueImpl {
    boolean isEmpty();
    void makeEmpty();
    void enqueue(int data);
    int dequeue();
    void print();
}
