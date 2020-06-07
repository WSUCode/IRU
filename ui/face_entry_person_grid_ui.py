

import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time
from setting import _
from _ui._face_entry import FaceEntry, VideoCapture

def iru_person_grid( window : tkinter.Tk ):

    name_label = tkinter.Label(
        window, text = _('name')
    )
    name_entry = tkinter.Entry(
        window,
    )

    age_label = tkinter.Label(
        window, text = _('age')
    )
    age_entry = tkinter.Entry(
        window,
    )
    
    gender_label = tkinter.Label(
        window, text = _('gender')
    )

    gender_entry = tkinter.Entry(
        window,
    )

    school_label = tkinter.Label(
        window, text = _('school')
    )
    school_entry = tkinter.Entry(
        window,
    )
    enrolling_date_label = tkinter.Label(
        window, text = _('enrolling date')
    )
    enrolling_date_entry = tkinter.Entry(
        window,
    )
    schooling_length_label = tkinter.Label(
        window, text = _('schooling length')
    )
    schooling_length_entry = tkinter.Entry(
        window,
    )


    name_label.grid( column=2, row=0 )
    name_entry.grid( column=3, row=0 )

    age_label.grid( column=2, row=1 )
    age_entry.grid( column=3, row=1 )

    gender_label.grid( column=2, row=2 )
    gender_entry.grid( column=3, row=2 )

    school_label.grid( column=2, row=3 )
    school_entry.grid( column=3, row=3 )

    enrolling_date_label.grid( column=2, row=4 )
    enrolling_date_entry.grid( column=3, row=4 )

    schooling_length_label.grid( column=2, row=5 )
    schooling_length_entry.grid( column=3, row=5 )