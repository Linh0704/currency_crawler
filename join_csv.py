import pandas as pd
import os

# Get the list of CSV files in the directory
csv_files = [file for file in os.listdir('data') if file.endswith('.csv')]

# Create an empty DataFrame to store the data
df = pd.DataFrame()

# Iterate over each CSV file
for file in csv_files:
    # Read the CSV file into a temporary DataFrame
    temp_df = pd.read_csv(os.path.join('data',file))
    
    # Extract the Date and Closing Price columns
    temp_df = temp_df[['Date', 'ClosingPrice']]
    
    # Rename the columns with the CSV file name
    filename = os.path.splitext(file)[0]
    temp_df.rename(columns={'ClosingPrice': filename}, inplace=True)
    
    # Set the Date column as the index
    temp_df.set_index('Date', inplace=True)
    
    # Append the temporary DataFrame to the main DataFrame
    df = pd.concat([df, temp_df], axis=1)

# Save the final DataFrame as a new CSV file
print(df)
df.to_csv('combined_data.csv', encoding='utf-8')
# df.to_csv('D:\\bae\\crawl_coinmarketcap\\custom\\currency_crawler\\combined_data.csv', encoding='utf-8')