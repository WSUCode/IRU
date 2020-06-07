
import os
import pickle
import tkinter
from tkinter import messagebox
from ui.face_entry_ui import face_entry
from ui.face_recg_ui import face_recg
from setting import _

class MainUI:
    def __init__(
        self,
        window: tkinter.Tk  ):

        self.faces_path = './data/iru.db'
        pass

    def to_face_recg(self):
        face_recg()

    def to_face_entry(self):
        face_entry()
    
    def get_iru_persons( self ):
        if os.path.exists( self.faces_path ):

            with open( self.faces_path , 'rb' ) as f:
                return pickle.load( f )

        else: 
            messagebox.showinfo( message = _('Nothing was read') )
    
    def save_iru_persons( self , iru_persons ):
        with open( self.faces_path , 'wb' ) as f:
            pickle.dump( iru_persons, f )
