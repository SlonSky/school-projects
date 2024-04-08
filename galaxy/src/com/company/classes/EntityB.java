package com.company.classes;

import java.awt.*;

/**
 * Created by Slon on 01.03.2016.
 */
public interface EntityB {
    public void tick();
    public void render(Graphics g);
    public Rectangle getBounds();
    public double getX();
    public double getY();
}
