package com.company;

import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

/**
 * Created by Slon on 01.03.2016.
 */
public class MouseInput implements MouseListener {
    @Override
    public void mouseClicked(MouseEvent e) {

    }

    @Override
    public void mousePressed(MouseEvent e) {
        int mx = e.getX();
        int my = e.getY();

        if(Game.state == Game.STATE.MENU) {
            if (mx >= Game.WIDTH / 2 + 120 && mx < Game.WIDTH / 2 + 220) {
                if (my >= 150 && my <= 200) {
                    Game.state = Game.STATE.GAME;
                    Game.score = 0;
                    Game.health = 100;
                }
            }
            if (mx >= Game.WIDTH / 2 + 120 && mx < Game.WIDTH / 2 + 220) {
                if (my >= 250 && my <= 300) {
                    Game.state = Game.STATE.MENU_HELP;
                }
            }
            if (mx >= Game.WIDTH / 2 + 120 && mx < Game.WIDTH / 2 + 220) {
                if (my >= 350 && my <= 400) {
                    System.exit(0);
                }
            }
        } else if(Game.state == Game.STATE.GAME_OVER){
            if (mx >= Game.WIDTH - 100 && mx < Game.WIDTH + 100) {
                if (my >= Game.HEIGHT - 50 && my <= Game.HEIGHT) {
                    Game.state = Game.STATE.MENU;
                }
            }
        } else if(Game.state == Game.STATE.MENU_HELP){
            if (mx >= Game.WIDTH*Game.SCALE - 200 && mx < Game.WIDTH*Game.SCALE - 100) {
                if (my >= Game.HEIGHT*Game.SCALE - 150 && my <= Game.HEIGHT*Game.SCALE - 50) {
                    Game.state = Game.STATE.MENU;
                }
            }
        }
    }

    @Override
    public void mouseReleased(MouseEvent e) {

    }

    @Override
    public void mouseEntered(MouseEvent e) {

    }

    @Override
    public void mouseExited(MouseEvent e) {

    }
}
