import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve,roc_auc_score,auc

read_path = "/home/con/mmdetection/data/thyroid/merge.xlsx"

data = pd.read_excel(read_path)


print(data.head())

# x=data.CL_확률[:1173]
x=data.OD_CL_확률변환[:236]
y=data.OD_CL_예측[:236]