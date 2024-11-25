package queue.queuelist;

public interface QueueListImpl {
    boolean isEmpty();
    void makeEmpty();
    void enqueue(int data);
    int dequeue();
    void print();
}
