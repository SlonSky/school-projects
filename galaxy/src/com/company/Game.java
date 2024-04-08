package com.company;

import com.company.classes.EntityA;
import com.company.classes.EntityB;
import sun.awt.image.ImageWatched;

import javax.sound.sampled.Clip;
import javax.swing.*;
import java.applet.Applet;
import java.applet.AudioClip;
import java.awt.*;
import java.awt.event.KeyEvent;
import java.awt.image.BufferStrategy;
import java.awt.image.BufferedImage;
import java.awt.image.Raster;
import java.io.File;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.LinkedList;

/**
 * Created by Slon on 29.02.2016.
 */
public class Game extends Canvas implements Runnable {

    public static final int WIDTH = 320;
    public static final int HEIGHT = WIDTH / 12 * 9;
    public static final int SCALE = 2;
    private final String TITLE = "GALAXY";

    private boolean running = false;
    private Thread thread;

    private BufferedImage image = new BufferedImage(WIDTH, HEIGHT, BufferedImage.TYPE_INT_RGB);
    private BufferedImage spriteSheet;
    private BufferedImage background = null;


    private boolean isShooting;

    private int enemyCount = 1;
    private int enemyKilled = 0;

    private Player p;
    private Controller c;
    private Textures textures;
    private Menu menu;
    private GameOver gameOver;
    private HelpMenu helpMenu;

    public LinkedList<EntityA> eA;
    public LinkedList<EntityB> eB;

    public static int health = 10;
    public static int score = 0;

    private Sound theme;
    private Sound shot;
    private Sound die;

    public enum STATE{
        MENU,
        MENU_HELP,
        GAME,
        GAME_OVER
    };

    public static STATE state = STATE.MENU;

    public void init(){
        requestFocus();
        spriteSheet = BufferedImageLoader.loadImage("res/spriteSheet.png");
        background = BufferedImageLoader.loadImage("res/background.png");

        addKeyListener(new KeyInput(this));
        addMouseListener(new MouseInput());

        textures = new Textures(this);
        c = new Controller(this, textures);
        p = new Player(200, 200, textures, this, c);
        menu = new Menu();
        gameOver = new GameOver();
        helpMenu = new HelpMenu();

        eA = c.getEntityA();
        eB = c.getEntityB();
        c.createEnemy(enemyCount);

        theme = new Sound(new File("res/sfx/theme.wav"));
        shot = new Sound(new File("res/sfx/shot.wav"));
        die = new Sound(new File("res/sfx/die.wav"));
        theme.play(false);
    }

    private synchronized void start(){
        if(running){
            return;
        }
        running = true;
        thread = new Thread(this);
        thread.start();
    }

    private synchronized void stop(){
        if(!running){
            return;
        }
        running = false;
        try {
            thread.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.exit(1);
    }

    @Override
    public void run() {
        init();
        long lastTime = System.nanoTime();
        final double amountOfTicks = 60.0;
        double ns = 1_000_000_000 / amountOfTicks;
        double delta = 0;
        int updates = 0;
        int frames = 0;
        long timer = System.currentTimeMillis();
        while (running){
            long now = System.nanoTime();
            delta += (now - lastTime) / ns;
            lastTime = now;
            if(delta >= 1){
                tick();
                updates++;
                delta--;
            }
            render();
            frames++;
            if(System.currentTimeMillis() - timer > 1000){
                timer += 1000;
                System.out.println(updates + " ticks, fps " + frames);
                updates = 0;
                frames = 0;
            }
        }
        stop();
    }

    private void tick(){
        if(state == STATE.GAME){
            p.tick();
            c.tick();
        }
        if(enemyKilled >= enemyCount){
            enemyCount += 2;
            enemyKilled = 0;
            c.createEnemy(enemyCount);
        }
    }

    private void render(){
        BufferStrategy bs = this.getBufferStrategy();
        if(bs == null){
            createBufferStrategy(3);
            return;
        }
        Graphics g = bs.getDrawGraphics();

        g.drawImage(image, 0, 0, getWidth(), getHeight(), this);
        g.drawImage(background, 0, 0, getWidth(), getHeight(), null);

        if(state == STATE.GAME) {
            p.render(g);
            c.render(g);

            g.setColor(Color.gray);
            g.fillRect(5, 5, 200, 10);

            g.setColor(Color.green);
            g.fillRect(5,5, 2 * health, 10);

            g.setColor(Color.white);
            g.drawRect(5, 5, 200, 10);

            if(health <= 0){
                state = STATE.GAME_OVER;
                die.play();
            }
        } else if(state == STATE.MENU){
            menu.render(g);
        } else if(state == STATE.GAME_OVER){
            gameOver.render(g);
        } else if(state == STATE.MENU_HELP){
            helpMenu.render(g);
        }
        g.dispose();
        bs.show();

    }
    public void keyPressed(KeyEvent e){
        int key = e.getKeyCode();
        if(state == STATE.GAME) {
            if (key == KeyEvent.VK_A) {
                p.setVelX(-5);
            } else if (key == KeyEvent.VK_D) {
                p.setVelX(5);
            } else if (key == KeyEvent.VK_S) {
                p.setVelY(5);
            } else if (key == KeyEvent.VK_W) {
                p.setVelY(-5);
            } else if (key == KeyEvent.VK_SPACE && !isShooting) {
                isShooting = true;
                c.addEntity(new Bullet(p.getX(), p.getY(), textures, this));
            }
        }
    }

    public void keyReleased(KeyEvent e){
        int key = e.getKeyCode();
        if(state == STATE.GAME) {
            if (key == KeyEvent.VK_A) {
                p.setVelX(0);
            } else if (key == KeyEvent.VK_D) {
                p.setVelX(0);
            } else if (key == KeyEvent.VK_S) {
                p.setVelY(0);
            } else if (key == KeyEvent.VK_W) {
                p.setVelY(0);
            } else if (key == KeyEvent.VK_SPACE) {
                isShooting = false;
                shot.play();
            }
        }
    }
    public static void main(String args[]){
        Game game = new Game();

        game.setPreferredSize(new Dimension(WIDTH * SCALE, HEIGHT * SCALE));
        game.setMaximumSize(new Dimension(WIDTH * SCALE, HEIGHT * SCALE));
        game.setMinimumSize(new Dimension(WIDTH * SCALE, HEIGHT * SCALE));



        JFrame frame = new JFrame(game.TITLE);
        frame.add(game);
        frame.pack();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setResizable(false);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);

        game.start();
    }

    public BufferedImage getSpriteSheet() {
        return spriteSheet;
    }

    public int getEnemyCount() {
        return enemyCount;
    }

    public void setEnemyCount(int enemyCount) {
        this.enemyCount = enemyCount;
    }

    public int getEnemyKilled() {
        return enemyKilled;
    }

    public void setEnemyKilled(int enemyKilled) {
        this.enemyKilled = enemyKilled;
    }
}
