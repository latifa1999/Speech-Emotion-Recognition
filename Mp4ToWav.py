"""
Use this script to convert MP4 files into Wav files.
"""

import os
import subprocess

# Loop through the filesystem
for root, dirs, files in os.walk("data/features", topdown=False):
    # Loop through files
    for name in files:
        # Consider only mp4
        if name.endswith('.mp4'):
            
            command = "ffmpeg -i /Users/Latifa/Desktop" + root[1:] + "/" + name + " " + "-ab 160k -ac 2 -ar 44100 -vn /Users/Latifa/Desktop/ConvertedFolder/"+  name[:-3] + "wav"
            
            # Execute conversion
            try:
                subprocess.call(command, shell=True)
                
            # Skip the file in case of error
            except ValueError:
                continue