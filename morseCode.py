from tkinter import *
import time
import RPi.GPIO as GPIO
import tkinter.font
from gpiozero import LED

led = LED(18)

def blinkMorse(sig):

        sig = str(sig)
        print(sig)
        sig = sig.split()
        
        
        for char in sig:
            for c in char:
                if c == '.':
                    led.on()
                    time.sleep(0.2)
                    led.off()
                    time.sleep(0.2)
                else:
                    led.on()
                    time.sleep(1)
                    led.off()
                    time.sleep(0.2)

def convertToMorse():

    morseWord = word.get()
    
    
    CODE = {'A': '.-',    'B': '-...',   'C': '-.-.',
                    'D': '-..',    'E': '.',      'F': '..-.',
                    'G': '--.',    'H': '....',   'I': '..',
                    'J': '.---',   'K': '-.-',    'L': '.-..',
                    'M': '--',     'N': '-.',     'O': '---',
                    'P': '.--.',   'Q': '--.-',   'R': '.-.',
                    'S': '...',    'T': '-',      'U': '..-',
                    'V': '...-',   'W': '.--',    'X': '-..-',
                    'Y': '-.--',   'Z': '--..'}
                    
    tempWord = str(morseWord)
    word.delete(0,tkinter.END)
    tempWord = tempWord.split()
    
    morseSig = " "
    
    for char in tempWord:
        for c in char:
            """print(CODE['A'])"""
            tempC = CODE[c.upper()]
            print(tempC)
            morseSig = morseSig + str(tempC)

    print("TEst : ",tempWord)
    blinkMorse(morseSig)

win = Tk()
win.title("Morse Code Converter")
myFont = tkinter.font.Font(family = "Ariel", size = 14 , weight = "bold")

tkinter.Label(win, text = "Enter Word").grid(row=0)

word = tkinter.Entry()
word.grid(row=0 , column =1)

entButton = Button(win , text = "Convert" , font = myFont , command = convertToMorse, height = 1 , width= 8 , bg = "green")
entButton.grid(row=1, column = 1)

exitButton = tkinter.Button(win , text="Exit" , command = win.quit , bg = "pink")
exitButton.grid(row=1 , column=0)


win.mainloop()
