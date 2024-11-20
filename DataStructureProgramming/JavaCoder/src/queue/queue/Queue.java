package queue.queue;

public class Queue implements QueueImpl {
    private final int[] array;
    private int front, back;

    public Queue() {
        array = new int[5];
        front = back = -1;
    }

    @Override
    public boolean isEmpty() {
        return (back==-1);
    }

    @Override
    public void makeEmpty() {
        front=back=-1;
        System.out.println("Queue berhasil dikosongkan");
    }

    @Override
    public void enqueue(int data) {
        if(isFull())
            System.out.println("Queue sudah penuh");
        else{
            if(isEmpty())
                front++;

            array[++back] = data;
            System.out.println("Data berhasil dimasukkan");
        }
    }

    @Override
    public int dequeue() {
        if(isEmpty())
            return -1;
        else{
            int awal = array[front];
            if(front==back)
                front = back = -1;
            else{
                geser();
                back--;
            }
            return awal;
        }
    }

    public boolean isFull() {
        return(back==array.length-1);
    }

    private void geser(){
        for(int i=front+1; i<=back; i++)
            array[i-1] = array[i];
    }

    public void print(){
        if(isEmpty())
            System.out.println("Tidak ada data dalam Queue");
        else
            for(int i=front;i<=back;i++)
                System.out.println(array[i]);
    }
}
