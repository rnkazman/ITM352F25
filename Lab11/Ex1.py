# Read in a CSV file and create a dataframe.  Print some info.
import pandas as pd
import ssl

# Temporary fix.  Don't do this in production code.
ssl._create_default_https_context = ssl._create_unverified_context
pd.set_option('display.max_columns', None)

url = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"

try:
    df = pd.read_csv(url, engine="pyarrow")
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    print(df.head())
    print(df.info())

except Exception as e:
    print(f"Error reading CSV: {e}"
          )
