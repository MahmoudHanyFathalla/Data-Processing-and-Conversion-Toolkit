import os
import pandas as pd
import json

# Define the folder paths
input_folder_path = 'C:\\Users\\hp\\Downloads\\ExtractingData\\data_excel'  # Folder containing Excel files
output_folder_path = 'C:\\Users\\hp\\Downloads\\ExtractingDataaaa\\output_json'  # Folder to save JSON files

# Create the output folder if it doesn't exist
os.makedirs(output_folder_path, exist_ok=True)

# Loop through all files in the input folder
for file_name in os.listdir(input_folder_path):
    if file_name.endswith('.xlsx'):
        # Full path to the Excel file
        file_path = os.path.join(input_folder_path, file_name)
        
        # Load the Excel file
        xls = pd.ExcelFile(file_path, engine='openpyxl')
        
        # Loop through all sheet names
        for sheet_name in xls.sheet_names:
            # Load the specific sheet
            df = pd.read_excel(xls, sheet_name=sheet_name)

            # Initialize variables for structured data extraction
            structured_data = {}
            current_title = df.iloc[0, 0]  # Treat the row before the first data row as the title
           # print(f"Title detected in {file_name} - sheet: {sheet_name}: {current_title}")
            structured_data[current_title] = []

            # Iterate through the rows starting from the row after the title
            for index, row in df.iloc[1:].iterrows():
                if pd.isnull(row[0]) == False and pd.isnull(row[1]) and pd.isnull(row[2]):
                    # Detected a new title section
                    current_title = row[0]
                  #  print(f"Title detected at index {index + 1} in {file_name} - sheet: {sheet_name}: {current_title}")
                    structured_data[current_title] = []
                elif current_title is not None:
                    # Add data rows to the current title's table
                    structured_data[current_title].append(row.tolist())

            # Convert the structured data into a more readable format (dictionary of DataFrames)
            structured_data = {title: pd.DataFrame(rows) for title, rows in structured_data.items()}

            # Convert the structured data into a JSON format
            structured_data_json = {title: df.fillna("").to_dict(orient='records') for title, df in structured_data.items()}

            # Define the output JSON file path
            output_file_name = f"{os.path.splitext(file_name)[0]}_{sheet_name}.json"
            json_file_path = os.path.join(output_folder_path, output_file_name)

            # Save the JSON data to a file
            with open(json_file_path, 'w', encoding='utf-8') as json_file:
                json.dump(structured_data_json, json_file, ensure_ascii=False, indent=4)

            print(f"JSON data has been saved to {json_file_path}")
