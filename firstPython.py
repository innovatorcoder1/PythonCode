import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import load_boston

boston = load_boston() # Load the boston dataset
df = pd.DataFrame(boston.data, columns=boston.feature_names) # Create a DataFrame

print(df.head())