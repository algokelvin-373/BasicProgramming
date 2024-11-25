package tree.bst;

public class BST {
    private Node akar;
    private static int ukuran = 0;
    public static int daun = 0;
    
    public boolean kosong() {
        return (akar == null);
    }

    public int getUkuran () {
        return ukuran;
    }

    public int leaf () {
        prosesLeaf (akar);
        return daun;
    }

    public void prosesLeaf (Node cabang) {
        if (cabang == akar)
            daun = 0;
        if (cabang != null) {
            if (cabang.kiri == null && cabang.kanan == null)
                daun++;
            prosesLeaf (cabang.kiri);
            prosesLeaf (cabang.kanan);
        }
    }

    public void insert (int data) {
        Node input = new Node(data);
        if (kosong()) {
            akar = input;
            this.ukuran++; }
        else {
            Node ortu = null;
            Node sekarang = akar;
            while (sekarang != null) {
                ortu = sekarang;
                if (sekarang.angka < data)
                    sekarang = sekarang.kanan;
                else
                    sekarang = sekarang.kiri; }
            if (ortu.angka < data)
                ortu.kanan = input;
            else
                ortu.kiri = input;
            input.orangtua = ortu;
            this.ukuran++;  }
        System.out.println ("Input data sukses\n");
    }

    public boolean find (int data) {
        boolean found = false;
        Node ortu = null;
        Node sekarang = akar;
        while (sekarang != null) {
            ortu = sekarang;
            if (sekarang.angka == data) {
                found = true;
                System.out.println ("Elemen "+sekarang.angka+" ada\n");
                break; }
            else if (sekarang.angka < data)
                sekarang = sekarang.kanan;
            else if (sekarang.angka > data)
                sekarang = sekarang.kiri;
            else
                System.out.println ("Data not found\n"); }
        return found;
    }

    public void inorder () {
        inorder (akar);
    }
    protected void inorder (Node akar) {
        if (akar == null)
            return;
        inorder (akar.kiri);
        System.out.print(akar.angka+" ");
        inorder (akar.kanan);
    }

    public void postorder () {
        postorder (akar);
    }
    protected void postorder (Node akar) {
        if (akar == null)
            return;
        postorder (akar.kiri);
        postorder (akar.kanan);
        System.out.print(akar.angka+" ");
    }

    public void preorder () {
        preorder (akar);
    }

    protected void preorder (Node akar) {
        if (akar == null)
            return;
        System.out.print(akar.angka+" ");
        preorder (akar.kiri);
        preorder (akar.kanan);
    }

    public void delete (int data) {
        Node ortu = null;
        Node sekarang = akar;
        if (kosong())
            System.out.println ("Data tree kosong\n");
        else {
            boolean found = find (data);
            if (found) {
                akar = prosesDelete (akar, data);
            }
            else
                System.out.println ("Data tidak ditemukan");
        }
    }

    public Node prosesDelete (Node akar, int data) {
        Node x, y, z;
        if(akar.getData() == data) {
            Node right, left;
            left = akar.getKiri();
            right = akar.getKanan();
            if (left == null && right == null) 
                return null;
            else if (left == null) {
                x = right;
                return x; }
            else if (right == null) {
                x = left;
                return x; }
            else {
                y = TemukanMin(right);
                x = right;
                while (x.getKiri() != null)
                    x = x.getKiri();
                x.setKiri(left);
                return y; } }
        if (data < akar.getData()) {
            z = prosesDelete(akar.getKiri(), data);
            akar.setKiri(z);
        }
        else {
            z = prosesDelete(akar.getKanan(), data);
            akar.setKanan(z);
        }
        System.out.println ("Data "+data+" telah ditemukan");
        this.ukuran--;
        return akar;
    }

    public Node TemukanMin (Node t) {
        if (t == null)
            return t;
        while (t.kiri != null)
            t = t.kiri;
        return t;
    }

    public void deleteAll () {
        ukuran = 0;
        akar = null;
        System.out.println ("Semua Data Telah Dihapus");
    }

    public void CariTerdekat (int data) {
        int prosesCari;
        if (kosong ())
            System.out.println ("Data tree kosong");
        else {
            prosesCari = Cari (data, akar, 0);
            if (prosesCari != 0)
                System.out.println ("\nData yang terdekat adalah "+prosesCari);
        }
    }

    public int Cari (int c, Node t, int a) {
        int ct = 0;
        boolean found = false;
        while (t != null) {
            if ((c+a)==t.angka || (c-a)==t.angka) {
                ct = t.angka;
                found = true;
                break;
            }
            else {
                if (c < t.angka)
                    t = t.kiri;
                else if (c > t.angka)
                    t = t.kanan;
            }
        }
        if (!found) {
            a++;
            ct = Cari (c, akar, a);
        }
        return ct;
    }

}
