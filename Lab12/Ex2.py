# Open a URL from the US Treasure and extract its information as a
# Dataframe.  Print the 1 month treasury rate.
import pandas as pd
import urllib.request

url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202410"

# Open the web page and save it as a DataFrame
print("Opening URL:", url)
try:
    tables = pd.read_html(url)
    int_rate_table = tables[0]  # Assuming the first table is the one we want
    #print(int_rate_table.columns)
    #print(int_rate_table.head())

    # Print the table of 1 month interest rates
    print("\n1 Month Treasury Rates:\n")
    for index, row in int_rate_table.iterrows():
        print(f"Index: {index}, Date: {row['Date']}, 1 Month Rate: {row['1 Mo']}")

except Exception as e:
    print("Error reading the URL or parsing HTML:", e)
    exit()