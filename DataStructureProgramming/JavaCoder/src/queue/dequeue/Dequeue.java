package queue.dequeue;

public class Dequeue implements DequeueImpl {
    private int[] array;
    private int front, back=-1;

    public Dequeue() {
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
        System.out.println("Queue telah dikosongkan");
    }

    @Override
    public void enqueue(int data) {
        if(isFull())
            doubleArray();
        if(isEmpty())
            front++;
        array[++back] = data;
        System.out.println("Data berhasil dimasukkan");
    }

    @Override
    public int dequeue() {
        if(isEmpty())
            return -1;
        else
        if(front==back){
            int d = array[front];
            front = back = -1;
            return d;
        }
        else
            return array[front++];
    }

    public boolean isFull(){
        return (back==array.length-1);
    }

    private void doubleArray(){
        int[] arr = new int[2*array.length];
        if(!isEmpty()){
            for(int i = front; i<=back; i++)
                arr[i] = array[i];
            array = arr;
        }
    }

    public void print(){
        if(isEmpty())
            System.out.println("Tidak ada data dalam Queue");
        else
            for(int i=front;i<=back;i++)
                System.out.println(array[i]);
    }
}
