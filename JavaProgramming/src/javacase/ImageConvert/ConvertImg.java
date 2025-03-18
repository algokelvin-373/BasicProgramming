package javacase.ImageConvert;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.IOException;
import java.util.Arrays;

public class ConvertImg {
    private final File file;
    private byte[] data;
    private String byteString;

    public ConvertImg(File file) {
        this.file = file;
    }

    public byte[] getData() {
        return data;
    }

    public String getByteString() {
        byteString = Arrays.toString(data);
        return byteString.replace(",", "")
                .replace("[", "")
                .replace("]", "");
    }

    public void convertImgToByte() throws IOException {
        BufferedImage bImage = ImageIO.read(file);
        ByteArrayOutputStream bos = new ByteArrayOutputStream();
        ImageIO.write(bImage, "png", bos );
        data = bos.toByteArray();
    }

    public void convertByteToImg(byte[] data) throws IOException {
        ByteArrayInputStream bis = new ByteArrayInputStream(data);
        BufferedImage bImage2 = ImageIO.read(bis);
        ImageIO.write(bImage2, "png", new File("output.png") );
        System.out.println("image created");
    }

    public String byteToHex(byte[] byteArray) {
        String hex = "";
        for (byte i : byteArray) {
            hex += String.format("%02X", i);
        }
        return hex;
    }

    public byte[] hexToByteArray(String hex) {
        byte[] ans = new byte[hex.length() / 2];
        for (int i = 0; i < ans.length; i++) {
            int index = i * 2;
            int val = Integer.parseInt(hex.substring(index, index + 2), 16);
            ans[i] = (byte)val;
        }
        return ans;
    }

}
