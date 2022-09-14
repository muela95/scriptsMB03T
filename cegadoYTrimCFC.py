from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
from random import *
import pandas as pd
import numpy as np

path = os.path.abspath(os.getcwd())
columnas = ["Nombre antiguo", "Nombre nuevo"]

print("Estamos en ", path)
filesOld = os.listdir(path)
videosOld = list(filter(lambda x: x.endswith(".mp4"), filesOld))
videosNew = []
print("Hay estos archivos ", filesOld)
print("Hay estos vídeos", videosOld)

for i in range(len(videosOld)):
    videosNew.insert(i, str(randint(10000000, 999999999))+".mp4")
    #os.rename(videosOld[i], str(videosNew[i]))
    ffmpeg_extract_subclip(videosOld[i], 150, 270, targetname=videosNew[i])


df = pd.DataFrame(list(zip(videosOld, videosNew)), columns=columnas)
df.to_excel("Ciego.xlsx")