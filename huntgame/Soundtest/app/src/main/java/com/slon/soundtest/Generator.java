package com.slon.soundtest;

import android.media.AudioFormat;
import android.media.AudioManager;
import android.media.AudioTrack;

/**
 * Created by Slon on 18.02.2017.
 */
public class Generator {
    private static AudioTrack track;
    private static final int SAMPLE_RATE = 44100;
    private static Thread thread;

    public static void playTrack(final int frequency, final int duration) {
        thread = new Thread(new Runnable() {
            @Override
            public void run() {
//                if(track.getPlayState() != AudioTrack.PLAYSTATE_PLAYING) {
                    track = writeSin(frequency, duration);
                    track.stop();
                    track.release();
//                }
            }
        });
        thread.start();
    }

    public static void stopTrack() {

//        thread.interrupt();
//        track.stop();
    }

    private static AudioTrack writeSin(int freq, int durationSec) {

        int bufferSize = AudioTrack.getMinBufferSize(
                SAMPLE_RATE,
                AudioFormat.CHANNEL_OUT_MONO,
                AudioFormat.ENCODING_PCM_8BIT);

        AudioTrack audioTrack = new AudioTrack(
                AudioManager.STREAM_MUSIC, SAMPLE_RATE,
                AudioFormat.CHANNEL_OUT_MONO,
                AudioFormat.ENCODING_PCM_16BIT,
                bufferSize, Au
                dioTrack.MODE_STREAM);

        double[] sound = new double[durationSec * SAMPLE_RATE];
        short[] buffer = new short[durationSec * SAMPLE_RATE];
        for(int i = 0; i < sound.length; i++) {
            sound[i] = Math.sin((2.0*Math.PI * i/(SAMPLE_RATE/freq)));
            buffer[i] = (short) (sound[i] * Short.MAX_VALUE);
        }

        audioTrack.setStereoVolume(AudioTrack.getMaxVolume(),AudioTrack.getMaxVolume());
        audioTrack.play();
        audioTrack.write(buffer, 0, sound.length);

        return  audioTrack;
    }
}
