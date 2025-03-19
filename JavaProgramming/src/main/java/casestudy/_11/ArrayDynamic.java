package com.linkedin._11;

public class ArrayDynamic {
    public static void main(String[] args) {
        DynamicArray array = new DynamicArray();
        array.add(10);
        array.add(20);
        array.add(30);
        array.add(40);
        array.add(50);
        int[] dt = array.getArray();
        for (int index = 0; index < dt.length - 1; index++) {
            System.out.println(dt[index]);
        }
    }
}

class DynamicArray {
    private int[] array;
    private int count = 0, size = 1;

    public DynamicArray() {
        this.array = new int[size];
    }
    public void add(int data) {
        array[count++] = data;
        updateSizeArray();
    }
    private void updateSizeArray() {
        int[] temp = new int[++size];
        int zero = 0;
        System.arraycopy(array, zero, temp, zero, array.length);
        array = temp;
    }
    public int[] getArray() {
        return array;
    }
}

