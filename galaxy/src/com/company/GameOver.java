package com.company;

import java.awt.*;
import java.awt.image.BufferedImage;

/**
 * Created by Slon on 02.03.2016.
 */
public class GameOver {
    public Rectangle buttonBack = new Rectangle(Game.WIDTH - 100, Game.HEIGHT - 50, 200, 50);
    public Rectangle scoreInfo = new Rectangle(Game.WIDTH - 125, Game.HEIGHT + 50, 250, 50);

    public void render(Graphics g){
        Graphics2D g2d = (Graphics2D)g;

        Font font = new Font("arial", Font.BOLD, 50);
        g.setFont(font);
        g.setColor(Color.WHITE);
        g.drawString("GAME OVER!", Game.WIDTH / 2, 100);

        Font font1 = new Font("arial", Font.BOLD, 30);
        g.setFont(font1);
        g.drawString("Back", buttonBack.x + 64, buttonBack.y + 32);
        g.drawString("Your score: " + Game.score, scoreInfo.x + 10, scoreInfo.y + 32);
        g2d.draw(buttonBack);
        g2d.draw(scoreInfo);
    }
}
