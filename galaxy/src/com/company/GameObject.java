package com.company;

import java.awt.*;

/**
 * Created by Slon on 01.03.2016.
 */
public class GameObject {
    public double x,y;

    public GameObject(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public Rectangle getBounds(int width, int height){
        return  new Rectangle((int)x, (int)y, width, height);
    }
}
