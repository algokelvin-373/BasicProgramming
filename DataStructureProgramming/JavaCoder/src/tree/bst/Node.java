package tree.bst;

public class Node {
    int angka;
    Node orangtua, kiri, kanan;

    public Node(int data) {
        this.angka = data;
        orangtua = kiri = kanan = null;
    }
    public Node getKiri () {
        return kiri;
    }
    public Node getKanan () {
        return kanan;
    }
    public int getData () {
        return angka;
    }
    public void setKiri (Node n) {
        kiri = n;
    }
    public void setKanan (Node n) {
        kanan = n;
    }
}
