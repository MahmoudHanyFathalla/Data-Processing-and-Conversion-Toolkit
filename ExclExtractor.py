import pandas as pd
import json

# Load the Excel file
file_path = 'C:\\Users\\hp\\Downloads\\ExtractingData\\data_excel\\01القاهرة.xlsx'  # Replace with your actual file path
xls = pd.ExcelFile(file_path, engine='openpyxl')

print(xls.sheet_names)
# Load the specific sheet
df = pd.read_excel(xls, sheet_name="أطباء القاهرة24")

# Initialize variables for structured data extraction
structured_data = {}
current_title = df.iloc[0, 0]  # Treat the row before the first data row as the title
print(f"Title detected at index 0: {current_title}")
structured_data[current_title] = []

# Iterate through the rows starting from the row after the title
for index, row in df.iloc[1:].iterrows():
    if pd.isnull(row[0]) == False and pd.isnull(row[1]) and pd.isnull(row[2]):
        # Detected a new title section
        current_title = row[0]
        print(f"Title detected at index {index + 1}: {current_title}")  # Adjust index to reflect the actual row number
        structured_data[current_title] = []
    elif current_title is not None:
        # Add data rows to the current title's table
        structured_data[current_title].append(row.tolist())

# Convert the structured data into a more readable format (dictionary of DataFrames)
structured_data = {title: pd.DataFrame(rows) for title, rows in structured_data.items()}

# Convert the structured data into a JSON format
structured_data_json = {title: df.fillna("").to_dict(orient='records') for title, df in structured_data.items()}

# Save the JSON data to a file
json_file_path = 'C:\\Users\\hp\\Downloads\\ExtractingData\\القاهgdfgdfgdfgره.json'  # Specify your output path

with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(structured_data_json, json_file, ensure_ascii=False, indent=4)

print(f"JSON data has been saved to {json_file_path}")
