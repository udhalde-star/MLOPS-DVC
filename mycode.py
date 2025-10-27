import pandas as pd
import os

# Create a sample DataFrame with column names
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# # Adding new row to df for V2
new_row_loc = {'Name': 'GF1', 'Age': 20, 'City': 'City1'}
df.loc[len(df.index)] = new_row_loc

# # Adding new row to df for V3
new_row_loc2 = {'Name': 'GF2', 'Age': 30, 'City': 'City2'}
df.loc[len(df.index)] = new_row_loc2

# --- Added more data rows below (no code logic changed) ---
df.loc[len(df.index)] = {'Name': 'David', 'Age': 40, 'City': 'Houston'}
df.loc[len(df.index)] = {'Name': 'Emma', 'Age': 22, 'City': 'Phoenix'}
df.loc[len(df.index)] = {'Name': 'Frank', 'Age': 28, 'City': 'Philadelphia'}
df.loc[len(df.index)] = {'Name': 'Grace', 'Age': 33, 'City': 'San Diego'}
df.loc[len(df.index)] = {'Name': 'Hannah', 'Age': 26, 'City': 'Dallas'}
df.loc[len(df.index)] = {'Name': 'Ian', 'Age': 38, 'City': 'Austin'}
df.loc[len(df.index)] = {'Name': 'Jack', 'Age': 29, 'City': 'San Jose'}
df.loc[len(df.index)] = {'Name': 'Kara', 'Age': 27, 'City': 'Seattle'}

# Ensure the "data" directory exists at the root level
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# Define the file path
file_path = os.path.join(data_dir, 'sample_data.csv')

# Save the DataFrame to a CSV file, including column names
df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")
