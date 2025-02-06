

import json

# Load the JSON data
with open('C:\\Users\\hp\\Downloads\\ExtractingData\\structured_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Create a text file to save the output
output_path = 'C:\\Users\\hp\\Downloads\\ExtractingData\structured_data.txt'
with open(output_path, 'w', encoding='utf-8') as txt_file:
    
    # Function to add section title
    def add_section_title(title):
        txt_file.write(f"\n{title}\n")
        txt_file.write("=" * len(title) + "\n")

    # Function to add content as paragraphs
    def add_paragraph_content(table):
        for row in table[1:]:  # Skip the header row
            txt_file.write(f"{row['1']} هو {row.get('2', 'غير محدد')} يمكن التواصل معه عبر الهاتف على الرقم {row['4']}. عنوانه {row.get('3', 'غير متوفر')}.\n")
        txt_file.write("\n")

    # Loop through the data and add content to the text file as paragraphs
    for section_title, table_data in data.items():
        add_section_title(section_title)
        add_paragraph_content(table_data)

print(f"Text file created successfully at {output_path}")