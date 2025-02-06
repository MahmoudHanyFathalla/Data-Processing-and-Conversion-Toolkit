import json
import os

# Define the folder containing the JSON files and the output folder for text files
input_folder_path = 'C:\\Users\\hp\\Downloads\\ExtractingData\\out_json\\optmized'
output_folder_path = 'C:\\Users\\hp\\Downloads\\ExtractingData\\out_txt\\optmized'

# Create the output folder if it doesn't exist
os.makedirs(output_folder_path, exist_ok=True)

# Function to add section title
def add_section_title(title, txt_file):
    txt_file.write(f"\n{title}\n")
    txt_file.write("=" * len(title) + "\n")

# Function to add content based on the table structure
def add_paragraph_content(table, txt_file):
    if table and isinstance(table, list) and len(table) > 0:
        # Get the header (first row) to determine the structure
        header = table[0]
        
        # Check if the table has the "الرجة العلمية" structure
        if header.get("1") == "الاسم" and header.get("2") == "الرجة العلمية" and header.get("3") == "العنوان" and header.get("4") == "التليفون":
            for row in table[1:]:  # Skip the header row
                name = row.get('1', 'غير متوفر')
                description = row.get('2', 'غير محدد')
                phone = row.get('4', 'غير متوفر')
                address = row.get('3', 'غير متوفر')
                txt_file.write(f"دكتور {name} هو {description} يمكن التواصل معه عبر الهاتف على الرقم {phone}. عنوانه {address}.\n")
        
        # Check if the table has the "العنوان" structure
        elif header.get("1") == "الاسم" and header.get("2") == "العنوان" and header.get("3") == "التليفون":
            for row in table[1:]:  # Skip the header row
                name = row.get('1', 'غير متوفر')
                description = row.get('2', 'غير محدد')
                phone = row.get('3', 'غير متوفر')
                txt_file.write(f"مستشفي او معمل {name} عنوانه {description} يمكن التواصل معه عبر الهاتف على الرقم {phone}.\n")
        
        # Default case: fallback if structure is not recognized
        else:
            for row in table[1:]:  # Skip the header row
                name = row.get('1', 'غير متوفر')
                description = row.get('2', 'غير محدد')
                phone = row.get('4', 'غير متوفر')
                address = row.get('3', 'غير متوفر')
                txt_file.write(f"{name} هو {description} يمكن التواصل معه عبر الهاتف على الرقم {phone}. عنوانه {address}.\n")
    
    txt_file.write("\n")

# Loop through all JSON files in the specified folder
for filename in os.listdir(input_folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(input_folder_path, filename)
        
        # Load the JSON data from each file
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
            # Create a corresponding text file for each JSON file
            output_filename = os.path.splitext(filename)[0] + '.txt'
            output_file_path = os.path.join(output_folder_path, output_filename)
            
            with open(output_file_path, 'w', encoding='utf-8') as txt_file:
                # Loop through the data and add content to the text file as paragraphs
                for section_title, table_data in data.items():
                    add_section_title(section_title, txt_file)
                    add_paragraph_content(table_data, txt_file)

print(f"Text files created successfully in {output_folder_path}")
