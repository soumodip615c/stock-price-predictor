import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("C:\\Users\\SOUMODIP\\Downloads\\archive (1)\\TCS Historical Data.csv")
#print(data.head())
data = data.drop(columns=["Unnamed: 0"])
data=data.rename(columns={"price" : "close"})
data=data.sort_values(by=["date"])






