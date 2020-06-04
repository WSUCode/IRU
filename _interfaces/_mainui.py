

from tkinter import filedialog
import tkinter
import cv2
from PIL import Image, ImageTk
import time
from iru import _
import face_recognition


class VideoCapture:
    def __init__(
        self, 
        video_source = 0):

        self.vid = cv2.VideoCapture(video_source)

        if not self.vid.isOpened():
            raise ValueError( \
                _( "Unable to open video source") , 
                video_source)

        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:

                return (ret, cv2.cvtColor(
                    frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()


class Commands:

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
        self.stop_getting_frame = False
    
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

    def  select_image(self):

        self.stop_getting_frame = True

        path = filedialog.askopenfilename(\
            filetypes=[("Image File",'.jpg')])

        if not path: 
            self.stop_getting_frame = False
            return

        self.frame = face_recognition.load_image_file( path )

        self.face_locations = face_recognition.face_locations( 
            self.frame )

        self.make_rect4face()

        self.place_image2tk()


    def snapshot(self):

        ret, self.frame = self.vid.get_frame()

        if ret:

            self.make_rect4face()

            self.stop_getting_frame = True

            self.place_image2tk()
            

    def update(self):

        if self.stop_getting_frame: return

        ret, self.frame = self.vid.get_frame()

        if ret:
            self.face_locations = face_recognition.face_locations(\
                self.frame)
            
            self.make_rect4face()
            self.place_image2tk()

        self.window.after( self.delay, self.update )