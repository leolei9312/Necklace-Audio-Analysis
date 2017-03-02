import pandas as pd
import librosa
import time
import numpy as np
import settings

def Labelize(feature, subj, length):
    label = []
    for i in range(length):
        if i >= 20:
            if i % 10 >= 0 and i % 10 <= 6:
                label.append(1)
            else:
                label.append(0)
        else:
            label.append(0)
    feature['Label'] = pd.Series(label, index = feature.index)
    feature.to_csv("Mydata/label/" + subj + "_label.csv")
