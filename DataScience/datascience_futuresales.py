import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Default theme
sns.set_theme()
df = pd.read_csv('dummydata.csv', usecols = ['occupation','vehicle_make', 'vehicle_year'])
df = df.head(500)

occupation = df['occupation']
vehicle = df['vehicle_make']
vehicle_year = df['vehicle_year']
sns.relplot(data=df, x=occupation, y=vehicle, hue=vehicle_year)
plt.savefig('save_as_a_png.png')