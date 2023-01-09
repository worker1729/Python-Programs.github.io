from moviepy.editor import *
mp4 = r"video.mp4"
mp3 = r"audio.mp3"

video = VideoFileClip(mp4)
audio = video.audio
audio.write_audiofile(mp3)
audio.close()
video.close()
