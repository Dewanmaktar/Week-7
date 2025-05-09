import pandas as pd

# Define the DataFrame (from 1. Accessing and Modifying the Index.py)
data = {'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'],
        'Age': [25, 30, 22, 35, 28],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
        'Salary': [50000, 55000, 40000, 70000, 48000]}

df = pd.DataFrame(data)

# Set 'Name' column as the index
df_with_index = df.set_index('Name')
print(df_with_index)