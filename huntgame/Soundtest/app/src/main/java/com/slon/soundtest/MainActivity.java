package com.slon.soundtest;

import android.media.AudioFormat;
import android.media.AudioManager;
import android.media.AudioTrack;
import android.media.ToneGenerator;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import static android.media.AudioFormat.CHANNEL_OUT_MONO;
import static android.media.AudioFormat.ENCODING_PCM_16BIT;
import static android.media.AudioFormat.ENCODING_PCM_8BIT;
import static android.media.AudioManager.STREAM_MUSIC;
import static android.media.ToneGenerator.TONE_CDMA_HIGH_PBX_S_X4;

public class MainActivity extends AppCompatActivity {
    ToneGenerator tg;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);





        Button b = (Button) findViewById(R.id.button2);
        b.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Generator.playTrack(Integer.parseInt(((EditText)findViewById(R.id.editText)).getText().toString()), 10);
                Toast.makeText(getBaseContext(), "played", Toast.LENGTH_SHORT).show();
            }
        });

        Button b2 = (Button) findViewById(R.id.button3);
        b2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Generator.stopTrack();
                Toast.makeText(getBaseContext(), "stopped", Toast.LENGTH_SHORT).show();
            }
        });


    }
}
