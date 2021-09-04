from mutagen.mp3 import MP3
import os

mp3_dir = os.listdir("/Volumes/Untitled/python_mutagen/mp3_meta_data/mp3s")
print (mp3_dir)
# function to convert the seconds into readable format
def convert(seconds):
    hours = seconds // 3600
    seconds %= 3600
    mins = seconds // 60
    seconds %= 60

    return hours, mins, seconds
# Create an MP3 object

for song in mp3_dir:
    if song.endswith(".mp3"):
        audio = MP3("/Volumes/Untitled/python_mutagen/mp3_meta_data/mp3s/" + song)
        audio_info = audio.info    
        length_in_secs = int(audio_info.length)
        hours, mins, seconds = convert(length_in_secs)
        print(song)
        #print("Hours:", hours)
        #print("Minutes:", mins)
        #print("Seconds:", seconds)
        print("Total Seconds", length_in_secs )

#TODO:
# COMMAND LINE ARGUMENT TO RUN SCRIPT IN ANY DIRECTORY 
# PRINT TRACK NUMBER
# https://pymediainfo.readthedocs.io/en/stable/