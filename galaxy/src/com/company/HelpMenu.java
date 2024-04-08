package com.company;

import java.awt.*;
import java.awt.image.BufferedImage;

/**
 * Created by Slon on 02.03.2016.
 */
public class HelpMenu {
    private BufferedImage bg = BufferedImageLoader.loadImage("res/help.png");
    private Rectangle back = new Rectangle(Game.WIDTH*Game.SCALE - 200, Game.HEIGHT*Game.SCALE - 150, 100, 50);

    public void render(Graphics g){
        g.drawImage(bg, 0,0, Game.WIDTH*Game.SCALE, Game.HEIGHT*Game.SCALE, null);
        Graphics2D g2d = (Graphics2D)g;
        Font font1 = new Font("arial", Font.BOLD, 30);
        g.setColor(Color.WHITE);
        g.setFont(font1);
        g.drawString("Back", back.x + 16, back.y + 32);
        g2d.draw(back);
    }
}
