package com.company;

import com.company.classes.EntityA;
import com.company.classes.EntityB;

import java.awt.*;
import java.util.Random;

/**
 * Created by Slon on 01.03.2016.
 */
public class Enemy extends GameObject implements EntityB {
    private Textures tex;
    private Animation anim;
    private Random r = new Random();

    private int speed = r.nextInt(3) + 1;

    private Game game;
    private Controller c;

    public Enemy(double x, double y, Textures tex, Controller c, Game game) {
        super(x,y);
        this.tex = tex;
        this.c = c;
        this.game = game;
        anim = new Animation(3, tex.enemy[0], tex.enemy[1], tex.enemy[2]);
    }

    public void tick(){
        y+= speed;
        if(y > Game.HEIGHT * Game.SCALE + 32){
            y = -16;
            x = r.nextInt(Game.WIDTH * Game.SCALE);
        }
        for(int i = 0; i < game.eA.size(); i++) {
            EntityA tempEnt = game.eA.get(i);
            if (Physics.Collision(this, tempEnt)) {
                c.removeEntity(this);
                c.removeEntity(tempEnt);
                game.score++;
                game.setEnemyKilled(game.getEnemyKilled() + 1);
            }
        }
        anim.runAnimation();
    }

    public void render(Graphics g){
        anim.drawAnimation(g, x, y, 0);
    }

    @Override
    public Rectangle getBounds() {
        return new Rectangle((int)x, (int)y, 32, 32);
    }

    public double getX() {
        return x;
    }

    public void setX(double x) {
        this.x = x;
    }

    public double getY() {
        return y;
    }

    public void setY(double y) {
        this.y = y;
    }
}
