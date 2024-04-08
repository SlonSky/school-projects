package com.company;

import com.company.classes.EntityA;
import com.company.classes.EntityB;
import sun.awt.image.ImageWatched;

import java.awt.*;
import java.util.LinkedList;
import java.util.Random;

/**
 * Created by Slon on 01.03.2016.
 */
public class Controller {
    private LinkedList<EntityA> eA = new LinkedList<>();
    private LinkedList<EntityB> eB = new LinkedList<>();
    EntityA entA;
    EntityB entB;
    Textures tex;
    Random r = new Random();
    private Game game;
    public Controller(Game game, Textures tex) {
        this.tex = tex;
        this.game = game;
//        addEntity(new Enemy(r.nextInt(Game.WIDTH * Game.SCALE), -16,tex, this, game));
    }

    public void tick(){
        for(int i = 0; i < eA.size(); i++){
            entA =  eA.get(i);

            entA.tick();
        }

        for(int i = 0; i < eB.size(); i++){
            entB =  eB.get(i);

            entB.tick();
        }
    }

    public void render(Graphics g){
        for(int i = 0; i < eA.size(); i++){
            entA =  eA.get(i);

            entA.render(g);
        }

        for(int i = 0; i < eB.size(); i++){
            entB =  eB.get(i);

            entB.render(g);
        }
    }

    public void createEnemy(int enemyCount){
        for(int i = 0; i < enemyCount; i++){
            addEntity(new Enemy(r.nextInt(Game.WIDTH * Game.SCALE), -16, tex, this, game));
        }
    }

    public void addEntity(EntityA block){
        eA.add(block);
    }

    public void removeEntity(EntityA block){
        eA.remove(block);
    }

    public void addEntity(EntityB block){
        eB.add(block);
    }

    public void removeEntity(EntityB block){
        eB.remove(block);
    }

    public LinkedList<EntityA> getEntityA(){
        return  eA;
    }

    public LinkedList<EntityB> getEntityB() {
        return eB;
    }
}
