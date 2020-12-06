# Authors: John Grider and Chris Rovero
# Date: 12/6/2020
# Purpose: Read and write data to and from an excel file to create visually appealing displays related to personal
# finance.

# List of Rovero tasks: 
# 1. Check for existing excel file in folder, if none exists create one.
# 2. Open the file, write some test data to it, and close it
# 3. Open the file, and read the data from it.

import os.path
if os.path.isfile('PersonalFinanceTracker.xlsx'):
    print('File exist')
else:
    from openpyxl import workbook
    book = workbook()
    sheet = book.active
    sheet['A1'] = 1500
    sheet['B1'] = 2500
    workbook.save(filename='PersonalFinanceTracker.xlsx')
    print('File not exist')

# List of Grider tasks:
# 1. Create GUI
# TESTING TESTING
