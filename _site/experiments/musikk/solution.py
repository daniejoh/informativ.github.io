from microbit import *
import music

while True:
    if button_a.is_pressed():
        music.play(music.FUNK)
    elif button_b.is_pressed():
        music.play(music.ODE)
