package binaryheap;

public class BinaryHeap {
    private int heapSize;
    public int[] heap;

    public BinaryHeap(int capacity) {
        heapSize = 0;
        heap = new int[capacity];
    }

    public boolean isEmpty( ) {
        return heapSize == 0;
    }

    public boolean isFull( ) {
        return heapSize == heap.length;
    }

    public void makeEmpty( ) {
        heapSize = 0;
    }

    private int parent(int i) {
        return (i - 1)/2;
    }

    private int kthChild(int i, int k) {
        return 2*i + k;
    }

    public void insert(int x) {

    }

    /*public int deleteMin() {

    }

    public int delete(int ind) {

    }*/

    private void heapifyUp(int childInd) {

    }

    private void heapifyDown(int ind) {

    }

    /** Function to get smallest child **/
    /*private int minChild(int ind) {

    }*/

    public void printHeap() {

    }
}
