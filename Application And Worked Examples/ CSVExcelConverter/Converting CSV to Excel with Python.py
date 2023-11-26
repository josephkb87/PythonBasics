Converting CSV to Excel with Python.py

# We will Converting a CSV file to Excel
# OpenPyXL to do the conversion from one file type to the other
# We will Converting an Excel spreadsheet to CSV


import csv
import openpyxl


def csv_to_excel(csv_file, excel_file):
    csv_data = []
    with open(csv_file) as file_obj:
        reader = csv.reader(file_obj)
        for row in reader:
            csv_data.append(row)

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    for row in csv_data:
        sheet.append(row)
    workbook.save(excel_file)


if __name__ == "__main__":
    csv_to_excel("books.csv", "books.xlsx")