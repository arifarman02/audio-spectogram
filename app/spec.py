import config
import librosa
import matplotlib
import moderngl
import numpy as np
import time

from utils import orthographic

hann = np.hanning(config.WINDOW_SIZE)

color_map = matplotlib.colormaps.get_cmap('inferno')


def stft_slice(window):
    n = window.shape[0]
    if n < WINDOW_SIZE:
        padded = np.zeros(WINDOW_SIZE, dtype=window.dtype)
        padded[:n] = window
        window = padded
    tapered = window * hann
    return np.fft.rfft(tapered)

def stft_color(slice, min_db=-50, max_db=30):
    slice = np.abs(slice)
    slice = librosa.amplitude_to_db(slice)
    slice = slice.clip(min_db, max_db)
    slice = (slice - min_db) / (max_db - min_db)
    slice = color_map(slice)
    slice = (slice * 255).astype('u1')
    slice = slice[:, :3]
    return slice



class Spec:

    VERTEX = '''
        #version 330 core
        uniform mat4 P;
        in vec2 vertex;
        in vec2 uv;
        out vec2 v_uv;
        void main() {
        gl_Position = P * vec4(vertex, 0, 1)};
        v_uv = uv;
        '''
    
    FRAGMENT = '''
        #version 330 core
        uniform sampler2D image;
        in vec2 v_uv;
        out vec4 out_color;
        void main() {
            vec4 color = texture(image, v_uv);
            out_color = vec4(color.rgb, 1)};
        '''
    
    def __init__(self, ctx, x, y, w, h):
        self.ctx = ctx
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.prog = self.ctx.program(
            vertec_shader=self.VERTEX,
            fragment_shader=self.FRAGMENT)
        
        vertices = np.array([
            0, y, 0, 0, #A
            0, y+h, 0, 1, #A
            w, y+h, 1, 1, #A
            0, y, 0, 0, #A
            0, y+h, 1, 1, #A
            0, y, 1, 0, #A
        ])