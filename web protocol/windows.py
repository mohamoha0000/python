# sender_windows.py
import socket
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
SERVER_IP = '192.168.1.2'
PORT = 50007

p = pyaudio.PyAudio()

# جرب تغيير 'Stereo Mix' حسب جهازك
def get_stereo_mix_index():
    keywords = ['stereo mix', 'mixage', 'stéréo']
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        name = info['name'].lower()
        print(name)
        if any(keyword in name for keyword in keywords):
            return i
    raise RuntimeError("Stereo Mix not found. تأكد من تفعيله من إعدادات الصوت.")

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                input_device_index=get_stereo_mix_index(),
                frames_per_buffer=CHUNK)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_IP, PORT))

print("Started sending audio...")
try:
    while True:
        data = stream.read(CHUNK, exception_on_overflow=False)
        s.sendall(data)
except KeyboardInterrupt:
    pass
finally:
    stream.stop_stream()
    stream.close()
    p.terminate()
    s.close()




"java code"


"""
package com.example.audioreceiver;

import android.app.Activity;
import android.media.AudioFormat;
import android.media.AudioManager;
import android.media.AudioTrack;
import android.os.Bundle;
import android.util.Log;

import java.io.InputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class MainActivity extends Activity {

    private boolean isRunning = true;
    private final int PORT = 50007;
    private final int SAMPLE_RATE = 44100;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        Thread serverThread = new Thread(new Runnable() {
            public void run() {
                try {
                    ServerSocket serverSocket = new ServerSocket(PORT);
                    Log.i("AudioServer", "Listening on port " + PORT);

                    while (isRunning) {
                        Socket clientSocket = serverSocket.accept();
                        Log.i("AudioServer", "Client connected");

                        InputStream inputStream = clientSocket.getInputStream();

                        int bufferSize = AudioTrack.getMinBufferSize(
                                SAMPLE_RATE,
                                AudioFormat.CHANNEL_OUT_STEREO,  // <-- Stereo to match sender
                                AudioFormat.ENCODING_PCM_16BIT
                        );

                        if (bufferSize < 2048) bufferSize = 2048;  // <-- زيادة حجم البفر إذا كان صغير

                        AudioTrack audioTrack = new AudioTrack(
                                AudioManager.STREAM_MUSIC,
                                SAMPLE_RATE,
                                AudioFormat.CHANNEL_OUT_STEREO,  // <-- مهم
                                AudioFormat.ENCODING_PCM_16BIT,
                                bufferSize,
                                AudioTrack.MODE_STREAM
                        );

                        audioTrack.play();

                        byte[] buffer = new byte[bufferSize];
                        int read;

                        while ((read = inputStream.read(buffer)) != -1) {
                            audioTrack.write(buffer, 0, read);
                            Thread.sleep(1);  // <-- يخفف الضغط على المعالج
                        }

                        audioTrack.stop();
                        audioTrack.release();
                        clientSocket.close();
                        Log.i("AudioServer", "Client disconnected");
                    }

                    serverSocket.close();
                } catch (Exception e) {
                    Log.e("AudioServer", "Error: " + e.getMessage());
                }
            }
        });

        serverThread.start();
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        isRunning = false;
    }
}
<uses-permission android:name="android.permission.INTERNET" />
https://chatgpt.com/share/68322d16-9f7c-8006-84be-15061dd8eee7
"""