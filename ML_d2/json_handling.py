import pandas as pd

# Loading Json data from the same folder
df = pd.read_json('train.json')
print(df.head())

# Displaying the shape of the DataFrame
print("DataFrame shape:", df.shape)
# Displaying the column names of the DataFrame
print("Column names:", df.columns.tolist())
# Displaying the data types of each column
print("Data types:\n", df.dtypes)
# Displaying summary statistics of the DataFrame
print("Summary statistics:\n", df.describe(include='all')) #check: count<total rows; min/max(not impossible); mean>median:right skew;large std:high variance/data spread out;high unique:encoding trickier
# Displaying the first few rows of the DataFrame
print("First few rows:\n", df.head())
# Displaying the last few rows of the DataFrame
print("Last few rows:\n", df.tail())
# Checking for missing values in each column
print("Missing values:\n", df.isnull().sum())

# Displaying unique values in each column
df["ingredients"] = df["ingredients"].apply(lambda x: ", ".join(x))#apply:runs a function on each row valuje in that column;lambds:anonymous function;join:joins list elements into a single string with specified separator
for column in df.columns:
    print(f"Unique values in '{column}':\n", df[column].unique())

# Displaying the count of unique values in each column
for column in df.columns:
    print(f"Value counts in '{column}':\n", df[column].value_counts())

# Displaying the correlation matrix for numerical columns
numeric_df = df.select_dtypes(include=["number"])
print("Correlation matrix:\n", numeric_df.corr())
# Displaying the index of the DataFrame
print("DataFrame index:", df.index)
# Displaying the columns of the DataFrame
print("Underlying numpy array:\n", df.values)
# Displaying the memory usage of the DataFrame
print("Memory usage:\n", df.memory_usage())

# chunking the DataFrame into smaller parts
chunk_size = 10000
for i in range(0, len(df), chunk_size):
    chunk = df[i:i + chunk_size]
    print(f"Chunk {i // chunk_size + 1}:\n", chunk)

#compression of DataFrame to json file
df.to_json('train_compressed.json', compression='gzip')
# Loading compressed Json data
df_compressed = pd.read_json('train_compressed.json', compression='gzip')
print("Compressed DataFrame shape:", df_compressed.shape)
# Displaying the first few rows of the compressed DataFrame
print("First few rows of compressed DataFrame:\n", df_compressed.head())

# encoding categorical columns
categorical_columns = df.select_dtypes(include=['object']).columns
for column in categorical_columns:
    df[column] = df[column].astype('category').cat.codes
print("DataFrame with encoded categorical columns:\n", df.head())

# handling nested JSON structures
nested_df = pd.json_normalize(df.to_dict(orient='records'))
print("Nested DataFrame shape:", nested_df.shape)
print("First few rows of nested DataFrame:\n", nested_df.head())
# Saving the modified DataFrame to a new JSON file
nested_df.to_json('train_nested.json', orient='records', lines=True)

# converting specific columns to datetime
datetime_columns = ['date_column1', 'date_column2']  # replace with actual date column names
for column in datetime_columns:
    if column in df.columns:
        df[column] = pd.to_datetime(df[column], errors='coerce')
print("DataFrame with datetime columns:\n", df.head())