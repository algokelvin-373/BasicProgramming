package javacase.ImageConvert;

import java.io.File;
import java.io.IOException;
import java.util.Arrays;

public class ImgToByte {
    public static void main(String[] args) throws IOException {
        String path = "src/javacase/ImageConvert/sample.png";
        ConvertImg imgConvert = new ConvertImg(new File(path));

        long start = System.currentTimeMillis();

        imgConvert.convertImgToByte();
        byte[] data = imgConvert.getData();
        String hex = imgConvert.byteToHex(data);
        int lengthHex = hex.length();

        long finish = System.currentTimeMillis();

        System.out.println("ByteString: "+ imgConvert.getByteString());
        System.out.println("\n");
        System.out.println("HexString: "+ hex);
        System.out.println("Length: "+ lengthHex);
        System.out.println("\n");

        System.out.println("Time execution: "+ (finish - start));

        // Convert back to Image
        start = System.currentTimeMillis();
        byte[] toByte = imgConvert.hexToByteArray(hex);
        imgConvert.convertByteToImg(toByte);
        finish = System.currentTimeMillis();

        System.out.println("Time execution: "+ (finish - start));

    }

}
