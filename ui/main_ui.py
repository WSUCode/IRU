

import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time
from setting import _
from _ui._main import MainUI

def main_ui():
    window = tkinter.Tk()
    _main_ui = MainUI( window )

    window.title( _('I Recognize U') )
    window.resizable(0,0)
    
    hello_label = tkinter.Label( 
        window, 
        text =  _('I Recognize U') ,
        font = ('', 66 )

    )

    to_face_entry = tkinter.Button(
        window, 
        text = _('Face entry'),
        command = _main_ui.to_face_entry
    )
    
    to_face_recg = tkinter.Button(
        window, 
        text = _('Face Recognize'),
        command = _main_ui.to_face_recg
    )
    
    about_label = tkinter.Button(
        window, 
        text = _('About'),
    )

    hello_label.grid(
        row = 0 , 
        column = 0,
        columnspan = 3
    )
    
    to_face_entry.grid(
        row = 1 , 
        column = 0
    )
    to_face_recg.grid(
        row = 1 , 
        column = 2
    )


    about_label.grid(
        row = 2 , 
        column = 1
    )

    window.mainloop()

    pass
    
    
