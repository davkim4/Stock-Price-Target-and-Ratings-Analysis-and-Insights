import pandas as pd

tesla_stockprice_df = pd.read_excel("combined_tesla.xlsx")
tesla_analyst_df = pd.read_excel("SELECTED_STOCKS.xlsx")

print(tesla_analyst_df.head())
