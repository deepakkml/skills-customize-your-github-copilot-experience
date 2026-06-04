# 📘 Assignment: Python File I/O & Data Persistence

## 🎯 Objective

Practice reading, writing, and persisting data in Python using text files, CSV files, and JSON files. This assignment teaches how to store program output so it can be reused later.

## 📝 Tasks

### 🛠️ Read and write a text file

#### Description
Create a program that reads content from a text file, processes it, and saves the result to a new file.

#### Requirements
Completed program should:

- Open and read a source text file using a context manager
- Transform or summarize the text in some way
- Write the processed content to a new text output file
- Print a summary showing how many lines were read and written
- Handle missing files gracefully with an error message

### 🛠️ Persist structured data with CSV and JSON

#### Description
Use Python’s standard libraries to save structured data in CSV and JSON formats, then reload it to confirm persistence.

#### Requirements
Completed program should:

- Create a list of dictionaries containing sample records
- Write the records to a CSV file with appropriate headers
- Read the CSV file back and print the loaded rows
- Save the same records to a JSON file
- Load the JSON file and print one record
- Use the `csv` and `json` modules for file handling
