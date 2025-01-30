package javacase.SecurityCaseStudy.AESKey;

import com.tsmid.tsmformula.TripleDESEncryptionV2;

import javax.crypto.NoSuchPaddingException;
import javax.crypto.SecretKey;
import java.security.NoSuchAlgorithmException;
import java.security.NoSuchProviderException;

public class EncAESKey {
    private static final char[] hexArray = "0123456789ABCDEF".toCharArray();
    private static TripleDESEncryptionV2 tsmCipher;

    public static void main(String[] args) throws NoSuchPaddingException, NoSuchAlgorithmException, NoSuchProviderException {
        byte[] aesKey = hexStringToByteArray("4CED412F4D415243484920444556454C4F504D454E542054534D46499633A655");
        tsmCipher = new TripleDESEncryptionV2(aesKey);
        byte[] iv = new byte[8];

        try {
            SecretKey secretKey = CryptoUtils.getAESKey(256);
            String plainAeskeyStr = bytesToHex(secretKey.getEncoded());
            System.out.println("plainAeskeyStr : "+ plainAeskeyStr);

            byte[] baAesKey = encrypt(hexStringToByteArray(plainAeskeyStr), iv);
            String aeskeyStr = bytesToHex(baAesKey);
            System.out.println("working: "+aeskeyStr);
        } catch (Exception e) {
            System.out.println("Internal Server Error [AU341]");
            throw new CustomException("Internal Server Error [AU341]");
        }
    }
    private static String bytesToHex(byte[] bytes) {
        char[] hexChars = new char[bytes.length * 2];
        for (int j = 0; j < bytes.length; j++) {
            int v = bytes[j] & 0xFF;
            hexChars[j * 2] = hexArray[v >>> 4];
            hexChars[j * 2 + 1] = hexArray[v & 0x0F];
        }
        return new String(hexChars);
    }
    private static byte[] hexStringToByteArray(String s) {
        int len = s.length();
        byte[] data = new byte[len / 2];
        for (int i = 0; i < len; i += 2) {
            data[i / 2] = (byte) ((Character.digit(s.charAt(i), 16) << 4) + Character.digit(s.charAt(i + 1), 16));
        }
        return data;
    }
    private static byte[] encrypt(byte[] rawText, byte[] iv) {
        try {
            return tsmCipher.encrypt(rawText, iv);
        } catch (Exception e) {
            e.printStackTrace();
            throw new CustomException("Invalid encrypt");
        }
    }
}
