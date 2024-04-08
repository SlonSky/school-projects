package com.company;

import java.awt.*;

/**
 * Created by Slon on 01.03.2016.
 */
public class Menu {

    public Rectangle playButton = new Rectangle(Game.WIDTH/2 + 120, 150, 100, 50);
    public Rectangle helpButton = new Rectangle(Game.WIDTH/2 + 120, 250, 100, 50);
    public Rectangle quitButton = new Rectangle(Game.WIDTH/2 + 120, 350, 100, 50);

    public void render(Graphics g){
        Graphics2D g2d = (Graphics2D)g;

        Font font = new Font("arial", Font.BOLD, 50);
        g.setFont(font);
        g.setColor(Color.WHITE);
        g.drawString("GALAXY", Game.WIDTH / 2 + 70, 100);

        Font font1 = new Font("arial", Font.BOLD, 30);
        g.setFont(font1);
        g.drawString("Play", playButton.x + 19, playButton.y + 32);
        g.drawString("Help", helpButton.x + 19, helpButton.y + 32);
        g.drawString("Quit", quitButton.x + 19, quitButton.y + 32);
        g2d.draw(playButton);
        g2d.draw(helpButton);
        g2d.draw(quitButton);
    }
}
