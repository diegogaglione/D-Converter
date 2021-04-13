import ffmpeg
import tkinter as tk
from tkinter import filedialog

print("File converter CLI by diwgo3sk")
print("Input file name including encoder (example: file.mp4)")
format = input()
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
stream = ffmpeg.input(file_path)
try:
    stream = ffmpeg.output(stream, format)
    print (format)
except:
    print("FFmpeg doesn't contains this encoder")
ffmpeg.run(stream)
