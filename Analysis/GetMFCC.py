# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 20:15:16 2017

@author: leo
"""

import pandas as pd
import librosa
import time
import numpy as np
import settings
import GenFeature

def getmfcc():
    for k in settings.Subjects:
        data = []
        temp = []
        audiopath = "data/audio/" + k + ".mp3"
        y, sr = librosa.load(audiopath)
        #mfcc
        mfccs = librosa.feature.mfcc(y=y, sr=sr)
        df = pd.DataFrame(data = mfccs)
        df = df.T
        #write into mfcc file without timestamp
        df.to_csv("Mydata/mfcc/" + k + ".csv")
         #get time of the audio
        for i in xrange(0, mfccs.shape[1]):
            temp.append(i)
        temp = librosa.frames_to_time(temp, sr=sr)
        for i in xrange(mfccs.shape[1]):
            temp[i] = temp[i] * 1000 + 1486844186207
         #add colum timestamp into df and write into csv
        df['timestamp'] = pd.Series(temp, index = df.index)
        print "Running get time."
        df.to_csv("Mydata/mfccwithtime/" + k + "_WithTime.csv")
        print "done!!!!!! " + k + "get time."
        print "running GenFeature"
        GenFeature.GenFeature(temp, sr, k)
        print "done getmfcc"
if __name__ == "__main__":
    getmfcc()
