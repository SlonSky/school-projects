package com.company;

import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

/**
 * Created by Slon on 01.03.2016.
 */
public class KeyInput extends KeyAdapter{

    Game game;

    public KeyInput(Game game) {
        this.game = game;
    }

    public void keyPressed(KeyEvent e){
        game.keyPressed(e);
    }

    public void keyReleased(KeyEvent e){
        game.keyReleased(e);
    }
}
