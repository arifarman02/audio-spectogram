from source import File
from window import Window



class App(Window):

    def init(self):
       self.source = File('audio/gettysburg.wav')

    def size(self, w, h):
        pass

    def draw(self, dt):
        pass



if __name__ == '__main__':
    App.run()