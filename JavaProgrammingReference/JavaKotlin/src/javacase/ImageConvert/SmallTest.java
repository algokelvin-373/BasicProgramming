package javacase.ImageConvert;

public class SmallTest {
    public static void main(String[] args) {
        byte[] b = new byte[]{'p', 'q', 'r'};

        System.out.print("Byte Array : ");
        for (byte an : b) {
            System.out.print(an + " ");
        }

        String hex = byteToHex(b);
        System.out.println("\nHex: "+ hex);

        byte[] ans = hexToByteArray(hex);

        // Printing the required Byte Array
        System.out.print("Byte Array : ");
        for (byte an : ans) {
            System.out.print(an + " ");
        }
    }

    public static String byteToHex(byte[] byteArray) {
        String hex = "";
        for (byte i : byteArray) {
            hex += String.format("%02X", i);
        }
        return hex;
    }

    public static byte[] hexToByteArray(String hex) {
        byte[] ans = new byte[hex.length() / 2];
        for (int i = 0; i < ans.length; i++) {
            int index = i * 2;
            int val = Integer.parseInt(hex.substring(index, index + 2), 16);
            ans[i] = (byte)val;
        }
        return ans;
    }

}
