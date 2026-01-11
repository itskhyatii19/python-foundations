import pandas as pd

# Loading dataset from the same folder locally. you need to paste the complete path if the dataset is in a different folder
df = pd.read_csv("StudentPerformance.csv")

print("Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

print("\nDataset info:")
print(df.info())

print("\nStatistical summary:")
print(df.describe())

print("\nMissing values:")
print(df.isnull().sum())

# Loading dataset from a URL with custom headers to avoid access issues 
import requests
from io import StringIO

url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0"}
req = requests.get(url, headers=headers)
data = StringIO(req.text)

df=pd.read_csv(data)
print("\nDataset2 info",df.info())
print("\nShape:",df.shape)
print("\nStatistical summary:",df.describe())
print("\nMissing values:",df.isnull().sum())

# sep and names parameters
# Loading a TSV (tab-separated values) file with custom column names(since we didnt hsve column names in the dataset);(default sep=', so we need to specify sep='\t')
df_movies = pd.read_csv('movie_titles_metadata.tsv', sep='\t', names=['sno','name','release_year','rating','votes','genres'])
print("\nMovies Dataset info:")
df_movies.info()
print("\nShape:",df_movies.shape)
print("\nStatistical summary:",df_movies.describe())
print("\nMissing values:",df_movies.isnull().sum())

# index_col parameter
# Loading a CSV file with an index column(Usually done when the dataset has a unique identifier column that can be used for indexing and you dont want to use the default integer index)
df_train = pd.read_csv('aug_train.csv',index_col='enrollee_id')

# header parameter
# if the first row contains column names but pandas fails to recognize it due to formatting issues, you can use the header parameter to specify the correct row 
df_test = pd.read_csv("test.csv", header=1)
df_test.info()

# header parameter
#if you only want certain columns from the dataset, you can use the usecols parameter to load only those specific columns
df_cols = pd.read_csv('aug_train.csv',usecols=['enrollee_id','gender','education_level'])
print(df_cols.head())

# na_values parameter
# If the dataset uses a specific string to denote missing values (e.g., "NA", "N/A", "missing"), you can use the na_values parameter to specify these strings so that pandas can correctly identify and handle them as NaN.this is useful if you want to apply NaN handling techniques later.
df_na = pd.read_csv('aug_train.csv', na_values=['NA', 'N/A', 'missing'])
print("\nMissing values after na_values parameter:")
print(df_na.isnull().sum())

# Replacement for squeeze method to convert a single-column DataFrame to a Series
# usecols=["enrollee_id"] → reads only that column.
# df4["enrollee_id"] → extracts that column as a Series.
df4 = pd.read_csv("aug_train.csv", usecols=["enrollee_id"])
df4 = df4["enrollee_id"]  # convert column to Series
print(type(df4))  # <class 'pandas.core.series.Series'>

#skip rows parameter
df_skip = pd.read_csv('aug_train.csv', skiprows=2)  # skips the first 2 rows
print("\nShape after skipping rows:", df_skip.shape)
print(df_skip.head())

#nrows parameter
df_nrows = pd.read_csv('aug_train.csv', nrows=5)  # reads only the first 5 rows
print("\nShape after reading nrows:", df_nrows.shape)
print(df_nrows.head())

#dtype parameter
df_dtype = pd.read_csv('aug_train.csv', dtype={'enrollee_id': str, 'city_development_index': float, 'target': int})
print("\nData types after specifying dtype:")
print(df_dtype.dtypes)

#encoding parameter
#u can either specify the encoding of the CSV file or change the encoding using any code editor..eg:sublime text.
df_encoding = pd.read_csv('aug_train.csv', encoding='utf-8')

#skip bad lines parameter
#on_bad_lines='error'
# on_bad_lines='warn'
# on_bad_lines='skip' 
df_bad_lines = pd.read_csv('aug_train.csv', on_bad_lines='skip')  # skips bad lines
print("\nShape after skipping bad lines:", df_bad_lines.shape)

#handling dates(parse_dates parameter)
#generally read csv by default takes date columns in string format(object). to parse dates we use parse_dates parameter. works ONLY when proper date format exists.
df_dates = pd.read_csv('IPL Matches 2008-2020.csv',parse_dates=['date']).info()

#converters parameter
#If you want to apply a custom conversion function to a specific column while reading the CSV file
#Creating a function to rename team names
def rename(name):
    if name == "Royal Challengers Bangalore":
        return "RCB"
    else:
        return name
# Using the converters parameter to apply the rename function to the 'team1' column
df_convert = pd.read_csv('IPL Matches 2008-2020.csv',converters={'team1':rename})

#low_memory=False
#When dealing with large CSV files that may have mixed data types in columns, setting low_memory=False can help prevent dtype inference issues.
df_low_memory = pd.read_csv("file.csv", low_memory=False)

# Loading a huge dataset in chunks
dfs = pd.read_csv('aug_train.csv',chunksize=8000)
for chunks in dfs:
    print(chunks.shape)
