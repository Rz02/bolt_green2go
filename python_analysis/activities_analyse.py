# Linear algebra
import numpy as np
# Data processing
import pandas as pd
# List files in a given directory
import os
# Visualization
import matplotlib.pyplot as plt

activity_records = pd.read_csv("cases_data/activity_table_dataset.csv")
activity_records.head()
activity_emission = pd.read_csv("cases_data/emission_by_activity.csv")
activity_emission.head()

# print("The Dimension: ", activity_records.shape)
"""The Dimension:  (18503, 4)"""

# Distribution of each type of activity:
activity_records['Activity Name'].value_counts()

# Visualize the distribution:
activity_plot = activity_records['Activity Name'].value_counts().plot.bar(title='Count of each type of activity', figsize=(8,6))
activity_plot.set_xlabel('activity', size = 20)
activity_plot.set_ylabel('activity count', size = 20)

# plt.show()