import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

path= r'C:\Users\trabk\Pulpit\PythonProjects\DataVisualizationandAnalysis\player_statistics_cleaned_final.csv'
df=pd.read_csv(path)

df.fillna(0, inplace=True)


