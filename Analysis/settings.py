chronoFolder = '../data/labels/chrono/csv/'
processingFolder = '../data/processing/'
sensorFolder = '../data/sensor/'
cleanFolder = '../data/cleandata/'
testInterfaceTiming = '../data/onlineinterface.csv'
figureFolder = '../data/figures/'
audioFolder = '../data/audio/'
intervalFolder = '../data/intervals/'
mfccFolder = '../data/mfcc/'

samplingPeriod = 10		# 100hz, in terms of ms

import pandas as pd
swallowWindowSize = 1500 # window of error, i.e. if detect within 3s then it's correct
motionWindowSize = 500

featureWinSize = [(-500, 500), (-1000, 1000), (-1500,0), (0, 1500), (-2000, 500), (-500, 2000), (-3000, 0)]

#Subjects = ["subj16", "subj17","subj18","subj19","subj20","subj21","subj23", "subj25","subj26","subj27", "test"]
Subjects = ["ALCrunchy", "ALSoft", "ALDrink", "MLAll"]

birthGoPro = {	'subj16': 1477544384865,
				'subj17': 1477874149135,
				'subj18': 1478463846690,
				'subj19': 1478475703316,
				'subj20': 1478633910403,
				'subj21': 1478651637281,
				'subj23': 1478715981472,
				'subj25': 1479259352884,
				'subj26': 1479264285437,
				'subj27': 1479271257459,
				}

# timeDf = pd.read_csv('necklace/onlineinterface.csv', index_col='Subject')
#
# structuredStart = timeDf.structuredStart
# structuredEnd = timeDf.structuredEnd
