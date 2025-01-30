package javacase.SecurityCaseStudy;

//import org.bouncycastle.jce.provider.BouncyCastleProvider;
//import org.bouncycastle.util.encoders.Base64;

import javax.crypto.Cipher;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.NoSuchProviderException;
import java.security.Security;
import java.util.Arrays;

public class TripleDESEncryption {
    /*static {
//        Security.addProvider(new BouncyCastleProvider());
    }

    private final Cipher cipher;
    private final SecretKey secretKey;
    private IvParameterSpec ivParameterSpec;

    public TripleDESEncryption(byte[] aesKey)
            throws NoSuchAlgorithmException, NoSuchPaddingException, NoSuchProviderException {
        MessageDigest messageDigest = MessageDigest.getInstance("md5");
        final byte[] digestOfPassword = messageDigest.digest(aesKey);
        final byte[] keyBytes = Arrays.copyOf(digestOfPassword, 24);
        for (int j = 0, k = 16; j < 8; ) {
            keyBytes[k++] = keyBytes[j++];
        }
        this.secretKey = new SecretKeySpec(keyBytes, "DES");
        ivParameterSpec = new IvParameterSpec(new byte[8]);
        this.cipher = Cipher.getInstance("DESede/CBC/PKCS5Padding", "BC");
    }

    public byte[] encrypt(byte[] plainText, byte[] iv) throws Exception {
        try {
            ivParameterSpec = new IvParameterSpec(iv);
            cipher.init(Cipher.ENCRYPT_MODE, secretKey, ivParameterSpec);
            final byte[] base64Byte = Base64.encode(plainText);
            final byte[] encode = this.cipher.doFinal(base64Byte);
            return encode;
        } catch (Exception e) {
            throw new Exception(e.getMessage());
        }
    }

    public byte[] decrypt(byte[] plainEncrypt, byte[] iv) throws Exception {
        try {
            ivParameterSpec = new IvParameterSpec(iv);
            cipher.init(Cipher.DECRYPT_MODE, secretKey, ivParameterSpec);
            final byte[] decode = cipher.doFinal(plainEncrypt);
            byte[] base64 = Base64.decode(decode);
            return base64;
        } catch (Exception e) {
            throw new Exception(e.getMessage());
        }
    }*/
}
