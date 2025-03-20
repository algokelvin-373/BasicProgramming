package com.linkedin._15;

import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;

public class GreyImageProgram {
    public static void main(String[] args) {
        try {
            File fileImg = new File("src/com.linkedin/_14/sample_image.png");
            BufferedImage image = ImageIO.read(fileImg);
            int width = image.getWidth();
            int height = image.getHeight();

            GreyscaleImage greyscaleImage = new GreyscaleImage(width, height, image);
            greyscaleImage.convertToGreyScale();

            File outputImg = new File("src/com.linkedin/_15/output_image.png");
            ImageIO.write(greyscaleImage.getGreyScaleImage(), "png", outputImg);
            System.out.println("Greyscale Image is Success");

        } catch (Exception e) {
            System.err.println("Error: "+e);
        }
    }
}

class GreyscaleImage {
    private final int width, height;
    private final BufferedImage originalImage;

    public GreyscaleImage(int width, int height, BufferedImage originalImage) {
        this.width = width;
        this.height = height;
        this.originalImage = originalImage;
    }

    public void convertToGreyScale() {
        for (int h = 0; h < height; h++) {
            for (int w = 0; w < width; w++) {
                Color color = new Color(originalImage.getRGB(w, h));
                int colorGreyImage = valueGreyScale(color);
                Color newColor = new Color(colorGreyImage, colorGreyImage, colorGreyImage);
                originalImage.setRGB(w, h, newColor.getRGB());
            }
        }
    }

    public BufferedImage getGreyScaleImage() { return originalImage; }

    private int valueGreyScale(Color color) {
        int red = (int)(color.getRed() * 0.299);
        int green = (int)(color.getGreen() * 0.587);
        int blue = (int)(color.getBlue() * 0.114);
        return red + green + blue;
    }
}

