from moviepy.editor import *
from os import * 

def LOCGET(location):
    global loc
    loc = location
    
def main():
    list1 = list(listdir("Songs"))

    for x in range (0,len(list1)):
        video = VideoFileClip(os.path.join(f"Songs\\{list1[x]}"))
        video.audio.write_audiofile(os.path.join(f"{loc}\\{list1[x]}.mp3"))

if __name__ == "__main__":
    main()