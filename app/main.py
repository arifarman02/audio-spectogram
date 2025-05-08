from source import File
from wave import Wave
from window import Window



class App(Window):

    def init(self):
       self.source = File('audio/gettysburg.wav')

       self.wave = Wave(self.ctx, 0, 0, 1200, 720)

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