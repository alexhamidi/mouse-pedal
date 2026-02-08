from pynput import mouse
from pynput.mouse import Button
import mido
import time
# setup virtual port
port_name = 'IAC Driver Bus 1'
outport = mido.open_output(port_name)

def on_click(_1, _2, button, pressed, _3):
    if button == Button.left:
        if pressed:
            print("on")
            msg_on = mido.Message('control_change', channel=0, control=64, value=127)
            outport.send(msg_on)
        else:
            print("off")
            msg_off = mido.Message('control_change', channel=0, control=64, value=0)
            outport.send(msg_off)

with mouse.Listener(on_click=on_click) as listener:
    listener.join()
    outport.close()