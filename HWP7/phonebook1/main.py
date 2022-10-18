from os.path import exists
from CSV_creating import creating
from file_writing import writing_scv
from file_writing import writing_txt


path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

writing_scv()
writing_txt()