import pandas as pd
import numpy as np

# Create a DataFrame with column1 ranging from 0 to 999
data = pd.DataFrame({"column1": np.arange(1000), "column2": np.arange(0, 2000, 2)})

# Save the DataFrame to a CSV file
data.to_csv("training_set.csv", index=False)
