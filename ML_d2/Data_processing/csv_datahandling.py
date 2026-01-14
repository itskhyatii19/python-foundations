import pandas as pd
import requests
from io import StringIO


"""
File: csv_datahandling.py
Purpose: Demonstrates advanced pandas read_csv parameters
Author: Khyati Sharma
"""


def load_local_csv():
    """Load CSV from local path and perform EDA"""
    df_local = pd.read_csv("StudentPerformance.csv")

    print("\nLocal CSV Info")
    print("Shape:", df_local.shape)
    print(df_local.head())
    print(df_local.info())
    print(df_local.describe())
    print("Missing values:\n", df_local.isnull().sum())


def load_csv_from_url():
    """Load CSV from URL with custom headers"""
    url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    data = StringIO(response.text)

    df_url = pd.read_csv(data)

    print("\nURL CSV Info")
    print(df_url.info())
    print("Shape:", df_url.shape)
    print(df_url.describe())
    print("Missing values:\n", df_url.isnull().sum())


def load_tsv_file():
    """Load TSV file with custom column names"""
    df_movies = pd.read_csv(
        'movie_titles_metadata.tsv',
        sep='\t',
        names=['sno', 'name', 'release_year', 'rating', 'votes', 'genres']
    )

    print("\nTSV Dataset Info")
    print(df_movies.info())
    print("Shape:", df_movies.shape)
    print(df_movies.describe())
    print("Missing values:\n", df_movies.isnull().sum())


def index_and_header_handling():
    """Demonstrate index_col & header parameters"""
    df_train = pd.read_csv('aug_train.csv', index_col='enrollee_id')

    df_test = pd.read_csv("test.csv", header=1)
    print("\nHeader Handling")
    print(df_test.info())


def column_selection():
    """Read specific columns"""
    df_cols = pd.read_csv(
        'aug_train.csv',
        usecols=['enrollee_id', 'gender', 'education_level']
    )
    print("\nSelected Columns")
    print(df_cols.head())


def handle_na_values():
    """Custom missing value handling"""
    df_na = pd.read_csv(
        'aug_train.csv',
        na_values=['NA', 'N/A', 'missing']
    )

    print("\nMissing values after custom NA handling")
    print(df_na.isnull().sum())


def convert_to_series():
    """Convert single column dataframe to series"""
    df_series = pd.read_csv(
        "aug_train.csv",
        usecols=["enrollee_id"]
    )["enrollee_id"]

    print("\nSeries Type:", type(df_series))


def skip_and_limit_rows():
    """Skip rows and read limited rows"""
    df_skip = pd.read_csv('aug_train.csv', skiprows=2)
    print("\nAfter skipping rows:", df_skip.shape)

    df_nrows = pd.read_csv('aug_train.csv', nrows=5)
    print("\nFirst 5 rows:\n", df_nrows)


def enforce_dtypes():
    """Specify column datatypes"""
    df_dtype = pd.read_csv(
        'aug_train.csv',
        dtype={
            'enrollee_id': str,
            'city_development_index': float,
            'target': int
        }
    )

    print("\nData types enforced")
    print(df_dtype.dtypes)


def encoding_example():
    """Read CSV with encoding"""
    pd.read_csv('aug_train.csv', encoding='utf-8')


def handle_bad_lines():
    """Skip corrupt rows"""
    df_bad = pd.read_csv(
        'aug_train.csv',
        on_bad_lines='skip'
    )
    print("\nAfter skipping bad lines:", df_bad.shape)


def parse_dates_example():
    """Parse date columns"""
    df_dates = pd.read_csv(
        'IPL Matches 2008-2020.csv',
        parse_dates=['date']
    )
    print("\nDate parsing successful")


def converters_example():
    """Apply custom conversion using converters"""

    def rename(team):
        return "RCB" if team == "Royal Challengers Bangalore" else team

    df_convert = pd.read_csv(
        'IPL Matches 2008-2020.csv',
        converters={'team1': rename}
    )

    print("\nTeam rename applied")


def low_memory_example():
    """Handle mixed datatypes"""
    pd.read_csv("file.csv", low_memory=False)


def chunk_processing():
    """Read large file in chunks"""
    chunks = pd.read_csv(
        'aug_train.csv',
        chunksize=8000
    )

    print("\nChunk shapes:")
    for chunk in chunks:
        print(chunk.shape)


def main():
    load_local_csv()
    load_csv_from_url()
    load_tsv_file()
    index_and_header_handling()
    column_selection()
    handle_na_values()
    convert_to_series()
    skip_and_limit_rows()
    enforce_dtypes()
    encoding_example()
    handle_bad_lines()
    parse_dates_example()
    converters_example()
    low_memory_example()
    chunk_processing()


if __name__ == "__main__":
    main()
