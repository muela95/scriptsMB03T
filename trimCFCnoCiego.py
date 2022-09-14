from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
from random import *
import pandas as pd
import numpy as np

path = os.path.abspath(os.getcwd())

print("Estamos en ", path)
files = os.listdir(path)
videos = list(filter(lambda x: x.endswith(".mp4"), files))
print("Hay estos archivos ", files)
print("Hay estos vídeos", videos)

for i in range(len(videos)):
    ffmpeg_extract_subclip(videos[i], 150, 270, targetname="recorte"+videos[i])

