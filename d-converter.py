import ffmpeg
import os
import tkinter as tk
from tkinter import filedialog

#os.chdir("/Files")# Optional, for Windows 10 add complete path to Files folder or the program will be crash if uncomment.

root = tk.Tk() #Set alias for TKinter.
root.withdraw() #Set window method.

file_path = filedialog.askopenfilename() #Asks for path of file to be converted.
new_file_path = filedialog.asksaveasfilename() #Asks for name, encoder and path of converted file.
stream = ffmpeg.input(file_path) #Add file to be converted to ffmpeg input.
try:
    stream = ffmpeg.output(stream, new_file_path) #Save converted file.
except:
    print("FFmpeg doesn't contains this encoder") #Exceptions.
ffmpeg.run(stream) #Run ffmpeg
os.remove(file_path) #Deletes the copy of file to be converted in Files folder.
