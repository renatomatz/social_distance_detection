import sys
import os
import time

if __name__ == "__main__":
    duration = float(sys.argv[1])/1000
    left, sub = (0, 0) if len(sys.argv) <= 2 else (float(sys.argv[2]), duration)
    freq = 440  # Hz
    while left >= 0:
        time.sleep(duration)
        os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
        left -= sub*2

