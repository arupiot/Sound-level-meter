import sounddevice as sd
from numpy import linalg as LA
import numpy as np

duration = 10  # seconds

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    print (int(volume_norm))

with sd.Stream(callback=print_sound):
    sd.sleep(duration * 1000)
