import pandas as pd
import sys
 
# Load the Excel file
excel_file_path = 'Java_Projects_Teams.xlsx'
df = pd.read_excel(excel_file_path)

# --- Debugging Step ---
# Print the first 5 rows and column names to identify the correct ones.
# Run `python process_dataset.py` and check the output in your terminal.
print("First 5 rows of the dataset:")
print(df.head())
print("\nColumn names in the dataset:")
print(df.columns)

# --- Action Required ---
# Replace 'YOUR_URL_COLUMN_NAME' and 'YOUR_LABEL_COLUMN_NAME' below with the actual column names from your file.
URL_COLUMN = 'YOUR_URL_COLUMN_NAME'
LABEL_COLUMN = 'YOUR_LABEL_COLUMN_NAME'

if URL_COLUMN == 'YOUR_URL_COLUMN_NAME' or LABEL_COLUMN == 'YOUR_LABEL_COLUMN_NAME':
    print("\n--- ACTION REQUIRED ---")
    print("Please open 'process_dataset.py' and replace 'YOUR_URL_COLUMN_NAME' and 'YOUR_LABEL_COLUMN_NAME' with the actual column names printed above.")
    sys.exit() # Stop the script until you edit the file.

# Extract 'URL' and 'Label' columns
urls_and_labels = df[[URL_COLUMN, LABEL_COLUMN]]

# Save to a CSV file
csv_file_path = 'phishing_urls.csv'
urls_and_labels.rename(columns={URL_COLUMN: 'URL', LABEL_COLUMN: 'Label'}).to_csv(csv_file_path, index=False)

print(f"Successfully extracted URLs and labels to {csv_file_path}")
