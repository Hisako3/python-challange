# %%
pip install pandas

# %%
import os
import pandas as pd

# %%
budget_df = pd.read_csv(r"C:Resources\budget_data.csv")
budget_df

# %%
month_count = budget_df['Date'].count()
profit_count = budget_df['Profit/Losses'].sum()
average_change = budget_df['Profit/Losses'].diff().mean().round(2)
max_change = budget_df['Profit/Losses'].diff().max().round()
max_change_date = budget_df.iloc[budget_df['Profit/Losses'].diff().idxmax(),0]
min_change = budget_df['Profit/Losses'].diff().min().round()
min_change_date = budget_df.iloc[budget_df['Profit/Losses'].diff().idxmin(),0]
print("Total Months:", month_count)
print("Total: $",profit_count)
print("Average Total: $",average_change)
print("Greatest Increaes in Profits:", max_change_date,"($",max_change,")")
print("Greatest Decreaes in Profits:",min_change_date,"($",min_change,")")


