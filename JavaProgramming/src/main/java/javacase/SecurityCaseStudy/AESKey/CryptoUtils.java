package javacase.SecurityCaseStudy.AESKey;

import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.GCMParameterSpec;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.SecretKeySpec;
import java.nio.ByteBuffer;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.security.spec.InvalidKeySpecException;
import java.security.spec.KeySpec;
import java.util.ArrayList;
import java.util.List;

public class CryptoUtils {

  private static final String ENCRYPT_ALGO = "AES/GCM/NoPadding";
  private static final int TAG_LENGTH_BIT = 128;
  private static final int IV_LENGTH_BYTE = 16;
  private static final int AES_KEY_BIT = 256;

  private static final Charset UTF_8 = StandardCharsets.UTF_8;

  public static byte[] getRandomNonce(int numBytes) {
    byte[] nonce = new byte[numBytes];
    new SecureRandom().nextBytes(nonce);
    return nonce;
  }

  // AES secret key
  public static SecretKey getAESKey(int keysize) throws NoSuchAlgorithmException {
    KeyGenerator keyGen = KeyGenerator.getInstance("AES");
    keyGen.init(keysize, SecureRandom.getInstanceStrong());
    return keyGen.generateKey();
  }

  // Password derived AES 256 bits secret key
  public static SecretKey getAESKeyFromPassword(char[] password, byte[] salt)
      throws NoSuchAlgorithmException, InvalidKeySpecException {

    SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
    // iterationCount = 65536
    // keyLength = 256
    KeySpec spec = new PBEKeySpec(password, salt, 65536, 256);
    SecretKey secret = new SecretKeySpec(factory.generateSecret(spec).getEncoded(), "AES");
    return secret;
  }

  // AES-GCM needs GCMParameterSpec
  public static byte[] encrypt(byte[] pText, SecretKey secret, byte[] iv) throws Exception {

    Cipher cipher = Cipher.getInstance(ENCRYPT_ALGO);
    cipher.init(Cipher.ENCRYPT_MODE, secret, new GCMParameterSpec(TAG_LENGTH_BIT, iv));
    byte[] encryptedText = cipher.doFinal(pText);
    return encryptedText;
  }

  // prefix IV length + IV bytes to cipher text
  public static byte[] encryptWithPrefixIV(byte[] pText, SecretKey secret, byte[] iv)
      throws Exception {

    byte[] cipherText = encrypt(pText, secret, iv);

    byte[] cipherTextWithIv =
        ByteBuffer.allocate(iv.length + cipherText.length).put(iv).put(cipherText).array();
    return cipherTextWithIv;
  }

  public static String decrypt(byte[] cText, SecretKey secret, byte[] iv) throws Exception {

    Cipher cipher = Cipher.getInstance(ENCRYPT_ALGO);
    cipher.init(Cipher.DECRYPT_MODE, secret, new GCMParameterSpec(TAG_LENGTH_BIT, iv));
    byte[] plainText = cipher.doFinal(cText);
    return new String(plainText, UTF_8);
  }

  public static String decryptWithPrefixIV(byte[] cText, String aesKey) throws Exception {

    ByteBuffer bb = ByteBuffer.wrap(cText);

    byte[] iv =
        hexStringToByteArray(
            "3F5D4F9F06CC7B403162AF23EFACBD12"); // new byte[IV_LENGTH_BYTE];
    // bb.get(iv);
    // bb.get(iv, 0, iv.length);

    byte[] cipherText = new byte[bb.remaining()];
    bb.get(cipherText);

    SecretKey secret = new SecretKeySpec(hexStringToByteArray(aesKey), "AES");

    String plainText = decrypt(cipherText, secret, iv);
    return plainText;
  }

  // hex representation
  public static String hex(byte[] bytes) {
    StringBuilder result = new StringBuilder();
    for (byte b : bytes) {
      result.append(String.format("%02x", b));
    }
    return result.toString();
  }

  // print hex with block size split
  public static String hexWithBlockSize(byte[] bytes, int blockSize) {

    String hex = hex(bytes);

    // one hex = 2 chars
    blockSize = blockSize * 2;

    // better idea how to print this?
    List<String> result = new ArrayList<>();
    int index = 0;
    while (index < hex.length()) {
      result.add(hex.substring(index, Math.min(index + blockSize, hex.length())));
      index += blockSize;
    }

    return result.toString();
  }
  public static byte[] hexStringToByteArray(String s) {
    int len = s.length();
    byte[] data = new byte[len / 2];
    for (int i = 0; i < len; i += 2) {
      data[i / 2] =
              (byte) ((Character.digit(s.charAt(i), 16) << 4) + Character.digit(s.charAt(i + 1), 16));
    }
    return data;
  }
}
