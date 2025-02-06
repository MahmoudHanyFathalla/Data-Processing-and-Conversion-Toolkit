import pandas as pd
import json

# Load the Excel file
file_path = 'your_excel_file.xlsx'  # Replace with your file path
xls = pd.ExcelFile(file_path)

# Initialize a dictionary to hold the structured JSON data
structured_data = {}

# Loop through each sheet and extract tables
for sheet_name in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet_name)
    
    current_category = None
    for index, row in df.iterrows():
        service_name = row['اسم الخدمة (1)']
        total_service = row['اجمالي الخدمة']
        contribution_family = row['المساهمة للعضو وأسرته']
        contribution_parents = row['المساهمة للوالدين']
        
        # Check if the row is a category
        if pd.isna(total_service) and pd.isna(contribution_family) and pd.isna(contribution_parents):
            current_category = service_name
            structured_data[current_category] = []
        else:
            if current_category is not None:
                structured_data[current_category].append({
                    "service_name": service_name,
                    "total_service": total_service,
                    "contribution_family": contribution_family,
                    "contribution_parents": contribution_parents
                })

# Convert the structured data to JSON
structured_json_data = json.dumps(structured_data, ensure_ascii=False, indent=4)

# Save the structured JSON data to a file
output_file_path = 'structured_data.json'
with open(output_file_path, 'w', encoding='utf-8') as f:
    f.write(structured_json_data)

print("Structured JSON data saved to:", output_file_path)
