package com.company;

import javax.sound.sampled.*;
import javax.xml.bind.Unmarshaller;
import java.io.File;
import java.io.IOException;

/**
 * Created by Slon on 02.03.2016.
 */
public class Sound {
    private Clip clip;
    private boolean isPlaying = false;

    public Sound(File f){
        try {
            AudioInputStream stream = AudioSystem.getAudioInputStream(f);
            clip = AudioSystem.getClip();
            clip.open(stream);
            clip.addLineListener(new Listener());

        } catch (Exception e) {
            e.printStackTrace();
        }



    }

    public boolean isPlaying() {
        return isPlaying;
    }

    public void play(boolean replay){
        if(replay){
            clip.stop();
            clip.setFramePosition(0);
            clip.start();
            isPlaying = true;
        } else if(!isPlaying){
            clip.setFramePosition(0);
            clip.start();
            isPlaying = true;
        }
    }

    public void play(){
        play(true);
    }

    public void stop(){
        if(isPlaying){
            clip.stop();
        }
    }

    private class Listener implements LineListener{

        @Override
        public void update(LineEvent event) {
            if(event.getType() == LineEvent.Type.STOP){
                isPlaying = false;
                synchronized (clip){
                    clip.notify();
                }
            }
        }
    }
}
