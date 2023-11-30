from tkinter import *
from moviepy.editor import *
from tkinter import filedialog
import tkinter.messagebox as messageb
from plyer import notification


video_path = filedialog.askopenfilename(title="Select a video file", filetypes=(("Video files", "*.mp4; *.mkv"), ("All files", "*.*")))

audio_path = filedialog.asksaveasfilename(title="Save audio file", defaultextension=".mp3",
                                          filetypes=(("Audio files", "*.mp3"), ("All files", "*.*")))
def notifications():
    notification.notify(
        title="status",
        message="file saved as mp3...",
        app_icon=None,
        timeout=10
    )

window = Tk()
window.title("convert mp4 to mp3")
window.geometry("500x500")
window.maxsize(width=500,height=500)
window.minsize(width=400,height=400)

text = Label(window,text="created by : sokan.py")
text.pack()

video = VideoFileClip(video_path)
video.audio.write_audiofile(audio_path)

if video :
    # message_ = messageb.showinfo("status","file saved as mp3...")
    notifications()


window.mainloop()
window.destroy()