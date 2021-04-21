import scipy.io as sio
import pandas as pd




baseline    = sio.loadmat('mat_files/baseline.mat')["baseline"]
bestpost    = sio.loadmat('mat_files/bestpost.mat')["bestpost"]
bestptb     = sio.loadmat('mat_files/bestptb.mat')["bestptb"]
mupost      = sio.loadmat('mat_files/mupost.mat')["mupost"]

optimalptb  = sio.loadmat('mat_files/optimalptb.mat')["optimalptb"]
oevpara     = sio.loadmat('mat_files/oevpara.mat')["oevpara"]
offset      = sio.loadmat('mat_files/offset.mat')["offset"]

signals     = sio.loadmat('mat_files/signals.mat')["signals"]
xmax_flu  = sio.loadmat('mat_files/xmax_flu.mat')["xmax_flu"]
xmin_flu  = sio.loadmat('mat_files/xmin_flu.mat')["xmin_flu"]
scale       = sio.loadmat('mat_files/scale.mat')["scale" ]


seasons = [ pd.date_range(start='1997', end='2008', freq='1Y'), pd.date_range(start='2010', end='2014', freq='1Y') ] # 1997-2007 and 2010-2013
regions = ['National','Region 1','Region 2','Region 3','Region 4','Region 5','Region 6','Region 7','Region 8','Region 9']

pathogens={'AH1','AH3','B','RSV','PIV12','PIV3'};




