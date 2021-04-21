import scipy.io as sio
import pandas as pd
import numpy as np

# load signals #national+10 regions
# load AH
# load xmax_flu
# load xmin_flu
# load oevpara


xmax_flu  = sio.loadmat('mat_files/xmax_flu.mat')["xmax_flu"]
xmin_flu  = sio.loadmat('mat_files/xmin_flu.mat')["xmin_flu"]
signals   = sio.loadmat('mat_files/signals.mat')["signals"]
scale     = sio.loadmat('mat_files/scale.mat')["scale"]



def ICfit_flu(season, region=0, scale, pid, ftime, signals, AH, xmax_flu, xmin_flu, oevpara):


    xmin = xmin_flu[:,region, pid]
    xmax = xmax_flu[:,region, pid]
    # check if there is activity
    threshold = 0.01
    activity  = 0
    onsetweek = 1

    obs    = signals[:ftime, pid+2, season, region]
    obs    = obs-min(obs)
    minidx = np.where(obs==np.min(obs))
    minidx = minidx[-1]


    return ic, pred