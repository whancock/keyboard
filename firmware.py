import asynio
from evdev import UInput, ecodes as e

ui = UInput()


ui.write(e.EV_KEY, e.KEY_A, 1)  # KEY_A down
ui.write(e.EV_KEY, e.KEY_A, 0)  # KEY_A up
ui.syn()


ui.close()