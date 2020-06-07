

from tkinter import filedialog
import tkinter
import cv2
from PIL import Image, ImageTk
import time
from setting import _
import face_recognition


class VideoCapture:
    def __init__(
        self, 
        video_source = 0):
        self.video_source = video_source

    
    def open_vidc(self):
        self.vid = cv2.VideoCapture(  self.video_source)

        if not self.vid.isOpened():
            raise ValueError( \
                _( "Unable to open video source") , 
                self.video_source)

        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        
        if not self.vid.isOpened():
            self.open_vidc()

        ret, self.frame = self.vid.read()
        if ret:

            return (ret, cv2.cvtColor(
                self.frame, cv2.COLOR_BGR2RGB))
        else:
            return (ret, None)
    

    def close_vidc(self):
        if self.vid.isOpened():
            self.vid.release()


class FaceEntry:

    def __init__(
        self,
        window: tkinter.Tk,
        vid:VideoCapture,
        canvas: tkinter.Canvas,
        delay = 15
        ):

        self.window = window
        self.vid = vid
        self.canvas = canvas
        self.delay = delay
        self.stop_updating_frame = False
    

    
    def place_image2tk(self):

        self.frame = ImageTk.PhotoImage(
            image = Image.fromarray( self.frame  ) )

        self.canvas.create_image(
            0, 0, image = self.frame, 
            anchor = tkinter.NW )

    def make_rect4face(self):

        self.face_locations = face_recognition.face_locations(
            self.frame)

        for top, right, bottom, left in self.face_locations:

            cv2.rectangle( self.frame, \
                (left, top), (right, bottom), (0, 0, 255), 2)




    def update_frame(self):

        if self.stop_updating_frame: return

        ret, self.frame = self.vid.get_frame()

        if ret:

            self.face_locations = face_recognition\
                .face_locations( self.frame )
            
            self.make_rect4face()
            self.place_image2tk()

        self.window.after( self.delay, self.update_frame )

    def recover_updating_frame(self):
        self.stop_updating_frame = False
        self.vid.open_vidc()
        self.update_frame()
    
    def stop_updating_frame_now(self):
        self.stop_updating_frame = True

    def close_face_entry(self):
        self.stop_updating_frame = True
        self.vid.close_vidc()
        self.window.destroy()

class WidgetCommand():
    
    def __init__( self, \
        face_entry:FaceEntry,
        snapshot_btn_text: tkinter.StringVar
        ):
        self.face_entry = face_entry
        self.snapshot_btn_text = snapshot_btn_text
        self.snapshot_btn_text.set( _('Snapshot') )
        self.is_face_entring = False
        

    def  select_image(self):

        self.face_entry.stop_updating_frame = True

        path = filedialog.askopenfilename(\
            filetypes=[("Image File",'.jpg')])

        if not path: 
            self.face_entry.stop_updating_frame = False
            return

        self.face_entry.frame = face_recognition.load_image_file( path )

        self.face_entry.face_locations = face_recognition.face_locations( 
            self.face_entry.frame )

        self.face_entry.make_rect4face()

        self.face_entry.place_image2tk()


    def snapshot(self):
        if not self.is_face_entring:
            ret, self.face_entry.frame = self.face_entry.vid.get_frame()

            if ret:

                self.face_entry.face_locations = face_recognition\
                    .face_locations(self.face_entry.frame)
                
                if len( self.face_entry.face_locations ) < 1:
                    self.snapshot_btn_text.set( _('Snapshot') )
                    self.is_face_entring = False
                    return

                self.snapshot_btn_text.set( _('Recover frame') )
                
                self.is_face_entring = True

                self.face_entry.stop_updating_frame_now()

                self.face_entry.make_rect4face()

                self.face_entry.place_image2tk()

                self.face_entry.vid.close_vidc()
        
        else:

            self.snapshot_btn_text.set( _('Snapshot') )
            self.is_face_entring = False
            self.face_entry.recover_updating_frame()