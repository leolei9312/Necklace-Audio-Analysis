import pandas as pd
import librosa
import time
import numpy as np
import settings
import Labelized
def GenFeature(time, sr, subj):
    df = pd.read_csv("Mydata/mfcc/" + subj + ".csv")
    endtime = (time[len(time) - 1] - time[0]) / 1000
    colnum = librosa.core.time_to_frames(np.arange(0, endtime, 1), sr = sr)
    winsize = 2
    cursec = 0
    data = []
    data = pd.DataFrame(data)
    feature = []
    feature = pd.DataFrame(feature)
    while cursec < len(colnum):
        k = winsize
        while k > 0:
            if cursec + k < len(colnum):
                data = data.append(df.loc[colnum[cursec] : colnum[cursec + k], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19']])
                break
            else:
                k = k - 1
        k = winsize
        while k > 0:
            if cursec - k >= 0:
                data = data.append(df.loc[colnum[cursec - k] : colnum[cursec], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19']])
                break
            else:
                k = k - 1
        mean = pd.DataFrame(data.mean()).T  #1. get mean
        for i in range(20):
            mean = mean.rename(columns = {str(i) : 'mfcc_mean_' + str(i)})
        min = pd.DataFrame(data.min()).T    #2. get min
        for i in range(20):
            min = min.rename(columns = {str(i) : 'mfcc_min_' + str(i)})
        max = pd.DataFrame(data.max()).T    #3. get max
        for i in range(20):
            max = max.rename(columns = {str(i) : 'mfcc_max_' + str(i)})
        std = pd.DataFrame(data.std()).T    #4. get std
        for i in range(20):
            std = std.rename(columns = {str(i) : 'mfcc_std_' + str(i)})
        median = pd.DataFrame(data.median()).T  #5. get median
        for i in range(20):
            median = median.rename(columns = {str(i) : 'mfcc_median_' + str(i)})
        skew = pd.DataFrame(data.skew()).T  #6. get skew
        for i in range(20):
            skew = skew.rename(columns = {str(i) : 'mfcc_skew_' + str(i)})
        rms = pd.DataFrame(np.sqrt((data ** 2).mean())).T   #7. get rms
        for i in range(20):
            rms = rms.rename(columns = {str(i) : 'mfcc_rms_' + str(i)})
        kurt = pd.DataFrame(data.kurt()).T  #8. get kurt
        for i in range(20):
            kurt = kurt.rename(columns = {str(i) : 'mfcc_kurt_' + str(i)})
        # quantile1 = pd.DataFrame(data.quantile(q=0.25)).T   #9. get quantile1
        # for i in range(20):
        #     quantile1 = quantile1.rename(columns = {str(i) : 'mfcc_quantile0.25_' + str(i)})
        # quantile2 = pd.DataFrame(data.quantile(q=0.75)).T   #10. get quantile2
        # for i in range(20):
        #     quantile2 = quantile1.rename(columns = {str(i) : 'mfcc_quantile0.75_' + str(i)})
        temp = pd.merge(mean, min, left_index = True, right_index = True)
        temp = pd.merge(temp, max, left_index = True, right_index = True)
        temp = pd.merge(temp, std, left_index = True, right_index = True)
        temp = pd.merge(temp, median, left_index = True, right_index = True)
        temp = pd.merge(temp, skew, left_index = True, right_index = True)
        temp = pd.merge(temp, rms, left_index = True, right_index = True)
        temp = pd.merge(temp, kurt, left_index = True, right_index = True)
        # temp = pd.merge(temp, quantile1, left_index = True, right_index = True)
        # temp = pd.merge(temp, quantile2, left_index = True, right_index = True)
        feature = feature.append(temp, ignore_index = True)
        temp.drop(temp.index, inplace = True)
        data.drop(data.index, inplace=True)
        cursec = cursec + 1
    print len(colnum)
    feature.to_csv("Mydata/mfccfeature/" + subj + "_Feature.csv")
    print "done GenFeature " + subj + " !!!"
    Labelized.Labelize(feature, subj, len(colnum))
