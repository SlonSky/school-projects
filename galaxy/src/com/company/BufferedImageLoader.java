package com.company;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

/**
 * Created by Slon on 01.03.2016.
 */
public class BufferedImageLoader {
    private static BufferedImage image;

    public static BufferedImage loadImage(String path) {
        try {
            image = ImageIO.read(new File(path));
        } catch (IOException e) {
            System.out.println("Can't load sprite sheet");
            e.printStackTrace();
        }
        return image;
    }
}
