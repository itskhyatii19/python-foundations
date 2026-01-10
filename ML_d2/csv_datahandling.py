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

# Loading a TSV (tab-separated values) file with custom column names(since we didnt hsve column names in the dataset);(default sep=', so we need to specify sep='\t')
# sep and names parameters
df_movies = pd.read_csv('movie_titles_metadata.tsv', sep='\t', names=['sno','name','release_year','rating','votes','genres'])
print("\nMovies Dataset info:")
df_movies.info()
print("\nShape:",df_movies.shape)
print("\nStatistical summary:",df_movies.describe())
print("\nMissing values:",df_movies.isnull().sum())

# Loading a CSV file with an index column(Usually done when the dataset has a unique identifier column that can be used for indexing and you dont want to use the default integer index)
# index_col parameter
df_train = pd.read_csv('aug_train.csv',index_col='enrollee_id')

# if the first row contains column names but pandas fails to recognize it due to formatting issues, you can use the header parameter to specify the correct row 
# header parameter
df_test = pd.read_csv("test.csv", header=1)
df_test.info()

#if you only want certain columns from the dataset, you can use the usecols parameter to load only those specific columns
# usecols parameter
df_cols = pd.read_csv('aug_train.csv',usecols=['enrollee_id','gender','education_level'])
print(df_cols.head())

# na_values parameter=If the dataset uses a specific string to denote missing values (e.g., "NA", "N/A", "missing"), you can use the na_values parameter to specify these strings so that pandas can correctly identify and handle them as NaN
df_na = pd.read_csv('aug_train.csv', na_values=['NA', 'N/A', 'missing'])
print("\nMissing values after na_values parameter:")
print(df_na.isnull().sum())

# Replacement for squeeze method to convert a single-column DataFrame to a Series
# usecols=["enrollee_id"] → reads only that column.
# df4["enrollee_id"] → extracts that column as a Series.
df4 = pd.read_csv("aug_train.csv", usecols=["enrollee_id"])
df4 = df4["enrollee_id"]  # convert column to Series
print(type(df4))  # <class 'pandas.core.series.Series'>

