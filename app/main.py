import config

from source import File, Microphone
from wave import Wave
from window import Window



class App(Window):

    def init(self):
       #self.source = File('audio/gettysburg.wav')
       self.source = Microphone()

       self.wave = Wave(self.ctx, 0, 0, config.WINDOW_WIDTH, config.WINDOW_HEIGHT)

    def size(self, w, h):
        self.wave.size(w, h)

    def draw(self, dt):
        available = self.source.available()
        window = self.source.get()
        print(available, window.shape if window is not None else None)

        self.wave.add(window)
        self.wave.update()
        self.wave.draw()



if __name__ == '__main__':
    App.run()