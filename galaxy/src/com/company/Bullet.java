package com.company;

import com.company.classes.EntityA;

import java.awt.*;
import java.awt.image.BufferedImage;

/**
 * Created by Slon on 01.03.2016.
 */
public class Bullet extends GameObject implements EntityA{

    private Textures tex;
    private Animation anim;
    private Game game;

    public Bullet(double x, double y, Textures tex, Game game){
        super(x, y);
        this.game = game;
        this.tex = tex;
        anim = new Animation(3, tex.missile[0], tex.missile[1], tex.missile[2]);
    }

    public void tick(){
        y -= 10;
        anim.runAnimation();
    }

    public void render(Graphics g){
        anim.drawAnimation(g, x, y, 0);
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    @Override
    public Rectangle getBounds() {
        return new Rectangle((int)x, (int)y, 32, 32);
    }
}
