import librosa
import math
import numpy as np
import pyaudio
import time

from utils import logger



class Source:
    
    def __init__(self, *args, **kwargs):
        self.audio = pyaudio.PyAudio()
        self.complete = False
        self.data = []
        self.index = 0
        self.total = 0
        self.init(*args, **kwargs)
    
    def init(self, *args, **Kwargs):
        raise NotImplementedError('source.init')
    
    def callback(self, data, frame_count, time_info, status):
        raise NotImplementedError('source.callback')
    


SAMPLE_RATE = 22050
BUFFER_SIZE = 1024



class File(Source):
    
    def init(self, filename):
        self.data, _ = librosa.load(filename, sr=SAMPLE_RATE)
        self.stream = self.audio.open(
            format=pyaudio.paFloat32,
            channels=1,
            rate=SAMPLE_RATE,
            output=True,
            frames_per_buffer=BUFFER_SIZE,
            stream_callback=self.callback)
        self.stream.start_stream()
    
    def callback(self, data, frame_count, time_info, status):
        a = self.total
        b = self.total + BUFFER_SIZE
        data = self.data[a:b]
        self.total = b
        if self.total >= len(self.data):
            self.complete = True
        return (data, pyaudio.paContinue)



class Microphone(Source):
    pass



if __name__ == '__main__':
    filename = './audio/gettysburg.wav'

    source = File(filename)

    time.sleep(5)