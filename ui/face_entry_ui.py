

import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time
from setting import _
from _ui._face_entry import FaceEntry, VideoCapture
from ui.face_entry_person_grid_ui import   iru_person_grid

def face_entry():
    
    face_entry_window = tkinter.Toplevel()
    vid = VideoCapture()
    vid.open_vidc()
    
    vid_canvas = tkinter.Canvas(
        face_entry_window, width = vid.width, 
        height = vid.height)

    _face_entry = FaceEntry( face_entry_window, vid, vid_canvas )

    snapshot_btn = tkinter.Button(
            face_entry_window, text= _("Snapshot"), 
            width=50, command= _face_entry.snapshot )

    select_image_btn = tkinter.Button(
            face_entry_window, text= _("Select image"), 
            width=50, command= _face_entry.select_image )
    

    face_entry_window.title ( _('IRU') )

    iru_person_grid( face_entry_window )

    vid_canvas.grid( 
        column = 0, row = 0 ,
        columnspan = 2 , rowspan = 7, )


    snapshot_btn.grid( column=2, row=6 )
    select_image_btn.grid( column=3, row=6 )

    
    _face_entry.update_frame()
    
    face_entry_window.protocol(
        "WM_DELETE_WINDOW", 
        _face_entry.close_face_entry )
    
    face_entry_window.mainloop()    
