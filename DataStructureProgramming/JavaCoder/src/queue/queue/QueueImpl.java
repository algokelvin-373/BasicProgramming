package queue.queue;

public interface QueueImpl {
    boolean isEmpty();
    void makeEmpty();
    void enqueue(int data);
    int dequeue();
    void print();
}
