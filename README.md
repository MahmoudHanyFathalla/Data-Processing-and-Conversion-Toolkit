# Data Processing and Conversion Toolkit

**Data Processing and Conversion Toolkit** is a collection of Python scripts designed to automate the conversion and processing of data across various formats, including **Excel**, **JSON**, **CSV**, **PDF**, and **Word documents**. This toolkit is particularly useful for handling large datasets, extracting structured data, and converting it into different formats for further analysis or reporting.

---

## Features

- **Excel to JSON Conversion**: Convert Excel files into structured JSON format, preserving table hierarchies and titles.
- **Excel to CSV Conversion**: Export Excel sheets into CSV files for easy data manipulation and analysis.
- **Excel to PDF Conversion**: Generate PDF reports from Excel data with customizable formatting.
- **JSON to Text Conversion**: Convert JSON data into readable text files, with support for structured content like tables and sections.
- **Excel to Word Conversion**: Extract data from Excel and create formatted Word documents.
- **Batch Processing**: Process multiple files in a directory, making it ideal for handling large datasets.
- **Customizable Output**: Control the structure and format of the output files to meet specific requirements.

---

## Project Structure

```
Data Processing Toolkit/
├── all_excel_to_json.py          # Converts all Excel files in a folder to JSON
├── all_json_to_txt.py            # Converts JSON files to structured text files
├── dataProcessing.py             # Processes Excel files into CSV, JSON, and PDF formats
├── ExclExtractor.py              # Extracts structured data from Excel and saves as JSON
├── exclToJson.py                 # Converts Excel sheets to JSON with custom structure
├── FromExeclToWord.py            # Converts Excel data into Word documents
├── json_to_txt.py                # Converts JSON files to text files (alternative script)
├── jsonToTxt.py                  # Converts JSON files to text files (alternative script)
├── README.md                     # Project documentation
└── requirements.txt              # List of dependencies
```

---

## Installation

### Prerequisites

- Python 3.8 or higher
- Required Python libraries (install via `requirements.txt`):
  ```bash
  pip install pandas openpyxl reportlab python-docx
  ```

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/Data-Processing-Toolkit.git
   cd Data-Processing-Toolkit
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### 1. **Excel to JSON Conversion**
   - **Script**: `all_excel_to_json.py`
   - **Description**: Converts all Excel files in a specified folder into JSON format, preserving table structures and titles.
   - **Usage**:
     ```bash
     python all_excel_to_json.py
     ```
   - **Input**: Folder containing Excel files.
   - **Output**: JSON files saved in the specified output folder.

### 2. **JSON to Text Conversion**
   - **Script**: `all_json_to_txt.py`
   - **Description**: Converts JSON files into structured text files, with support for tables and sections.
   - **Usage**:
     ```bash
     python all_json_to_txt.py
     ```
   - **Input**: Folder containing JSON files.
   - **Output**: Text files saved in the specified output folder.

### 3. **Excel to CSV, JSON, and PDF Conversion**
   - **Script**: `dataProcessing.py`
   - **Description**: Processes Excel files into CSV, JSON, and PDF formats in batch mode.
   - **Usage**:
     ```bash
     python dataProcessing.py
     ```
   - **Input**: Folder containing Excel files.
   - **Output**: CSV, JSON, and PDF files saved in their respective output folders.

### 4. **Excel to Word Conversion**
   - **Script**: `FromExeclToWord.py`
   - **Description**: Converts Excel data into formatted Word documents.
   - **Usage**:
     ```bash
     python FromExeclToWord.py
     ```
   - **Input**: Excel file with questions and answers.
   - **Output**: Word document with formatted content.

### 5. **Custom Excel to JSON Conversion**
   - **Script**: `exclToJson.py`
   - **Description**: Converts Excel sheets into JSON with a custom structure, ideal for specific data formats.
   - **Usage**:
     ```bash
     python exclToJson.py
     ```
   - **Input**: Excel file with a specific structure.
   - **Output**: JSON file with structured data.

### 6. **Excel Data Extraction**
   - **Script**: `ExclExtractor.py`
   - **Description**: Extracts structured data from Excel and saves it as JSON.
   - **Usage**:
     ```bash
     python ExclExtractor.py
     ```
   - **Input**: Excel file with structured data.
   - **Output**: JSON file with extracted data.

### 7. **JSON to Text Conversion (Alternative Scripts)**
   - **Scripts**: `json_to_txt.py` and `jsonToTxt.py`
   - **Description**: These scripts provide alternative methods for converting JSON files into text files. They are useful for different JSON structures or specific formatting requirements.
   - **Usage**:
     ```bash
     python json_to_txt.py
     ```
     or
     ```bash
     python jsonToTxt.py
     ```
   - **Input**: JSON files.
   - **Output**: Text files saved in the specified output folder.

---

## Customization

- **Input/Output Paths**: Modify the input and output folder paths in each script to match your file structure.
- **Data Structure**: Adjust the scripts to handle different Excel or JSON structures as needed.
- **PDF Formatting**: Customize the PDF generation in `dataProcessing.py` to match your reporting requirements.

---

## Example Workflow

1. **Convert Excel to JSON**:
   - Use `all_excel_to_json.py` to convert multiple Excel files into JSON format.
   
2. **Convert JSON to Text**:
   - Use `all_json_to_txt.py`, `json_to_txt.py`, or `jsonToTxt.py` to generate readable text files from the JSON data.

3. **Generate PDF Reports**:
   - Use `dataProcessing.py` to create PDF reports from Excel data.

4. **Create Word Documents**:
   - Use `FromExeclToWord.py` to generate Word documents from Excel data.

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **Pandas** for data manipulation.
- **OpenPyXL** for Excel file handling.
- **ReportLab** for PDF generation.
- **python-docx** for Word document creation.
- **All contributors** who helped in developing and testing this toolkit.

---

**Data Processing and Conversion Toolkit** is designed to simplify data handling and conversion tasks, making it easier to work with large datasets across multiple formats. Whether you're a data analyst, developer, or researcher, this toolkit will save you time and effort in processing and converting data.
