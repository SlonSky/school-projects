package com.company;

import java.awt.image.BufferedImage;

/**
 * Created by Slon on 01.03.2016.
 */
public class SpriteSheet {
    private BufferedImage image;

    public SpriteSheet(BufferedImage image){
        this.image = image;
    }

    public BufferedImage grabImage(int col, int row, int width, int height){
        BufferedImage img = image.getSubimage(col * width - width, row * height - height , width, height);
        return img;
    }

}
