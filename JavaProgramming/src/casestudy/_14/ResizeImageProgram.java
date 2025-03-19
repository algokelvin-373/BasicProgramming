package com.linkedin._14;

import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;

public class ResizeImageProgram {
    public static void main(String[] args) {
        try {
            File fileImg = new File("src/com.linkedin/_14/sample_image.png");
            BufferedImage image = ImageIO.read(fileImg);
            int width = image.getWidth();
            int height = image.getHeight();
            int type = image.getType();

            ResizeImage resizeImage = new ResizeImage(width, height, type, image);
            BufferedImage resize = resizeImage.setResizeImage(0.5f);

            File outputImg = new File("src/com.linkedin/_14/output_image.png");
            ImageIO.write(resize, "png", outputImg);
            System.out.println("Resize Image is Success");

        } catch (Exception e) {
            System.err.println("Error: "+e);
        }
    }
}

class ResizeImage {
    private final int width, height, type;
    private final BufferedImage originalImage;

    ResizeImage(int width, int height, int type, BufferedImage image) {
        this.width = width;
        this.height = height;
        this.type = type;
        this.originalImage = image;
    }

    public BufferedImage setResizeImage(int targetWidth, int targetHeight) {
        return resize(targetWidth, targetHeight);
    }

    public BufferedImage setResizeImage(float percent) {
        return resize((int)(percent * width), (int)(percent * height));
    }

    private BufferedImage resize(int targetWidth, int targetHeight) {
        BufferedImage resizeImage = new BufferedImage(targetWidth, targetHeight, type);
        Graphics2D graphics2D = resizeImage.createGraphics();
        graphics2D.drawImage(originalImage, 0, 0, targetWidth, targetHeight, null);
        graphics2D.dispose();
        return resizeImage;
    }
}

