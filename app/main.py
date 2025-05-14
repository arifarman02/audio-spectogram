import config

from rect import Rect
from source import File, Microphone
from spec import Spec
from wave import Wave
from window import Window

from utils import logger


class App(Window):

    def init(self):
       logger.info(f'init')
       
       self.source = Microphone()

       self.wave = Wave(self.ctx, 0, 0, config.WINDOW_WIDTH, 200)
       self.spec = Spec(self.ctx, 0, self.wave.h, config.WINDOW_WIDTH, 460)


       bg_color = (0.06, 0.06, 0.07, 1)

       # Time axis background colour
       self.r1 = Rect(self.ctx, 0, 660, config.WINDOW_WIDTH, 70, bg_color)

       # Frequency axis background colour
       self.r2 = Rect(self.ctx, 0, 0, 80, config.WINDOW_HEIGHT, bg_color)


    def size(self, w, h):
        logger.info(f'size {w} {h}')
        self.wave.size(w, h)
        self.spec.size(w, h)
        self.r1.size(w, h)
        self.r2.size(w, h)

    def draw(self, dt):
        available = self.source.available()
        window = self.source.get()

        logger.info(f'{available} {window.shape if window is not None else None}')

        self.wave.add(window)
        self.spec.add(window)

        self.wave.update()
        self.spec.update()

        self.wave.draw()
        self.spec.draw()

        self.r1.draw()
        self.r2.draw()
    
    def exit(self):
        logger.info('exit')
        self.source.release()



if __name__ == '__main__':
    App.run()