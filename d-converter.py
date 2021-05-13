import ffmpeg
import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image

#os.chdir("/Files")# Optional, for Windows 10 add complete path to Files folder or the program will be crash if uncomment.

video_encoders = open("data/encoders.txt", "r") #Open file with all video encoders
image_formats = open("data/formats.txt", "r") #Open file with image formats.
root = tk.Tk() #Set alias for TKinter.
root.withdraw() #Set window method.

file_path = filedialog.askopenfilename() #Asks for path of file to be converted.
new_file_path = filedialog.asksaveasfilename() #Asks for name, encoder and path of converted file.
stream = ffmpeg.input(file_path) #Add file to be converted to ffmpeg input.
if file_path in video_encoders.read(): #Check if in video encoders
    stream = ffmpeg.output(stream, new_file_path) #Save converted file.
    ffmpeg.run(stream) #Run ffmpeg
    os.remove(file_path) #Deletes the copy of file to be converted in Files folder.
else: #If other, images only are supported right now
    image_to_be_converted = Image.open(file_path) #Select image to be converted
    image_converted = image_to_be_converted.save(new_file_path) #Convert image
    
video_encoders.close() #Close file with all video encoders

