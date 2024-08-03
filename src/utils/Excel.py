import os
import openpyxl


class ExcelOperation:
    def __init__(self):
        self.file_name = "history_AI"
        self.file_path = os.getcwd() + "/../data/" + self.file_name + ".xlsx"
        self.workbook = openpyxl.load_workbook(self.file_path)
        self.sheet = self.workbook["history"]

    def add_new_image(self, prompt, name_image):
        print("Adding new image in history excel file...")
        new_line_size = self.sheet.max_row
        self.sheet['A' + str(new_line_size + 1)] = prompt
        self.sheet['B' + str(new_line_size + 1)] = name_image + "_" + str(new_line_size)
        print("New image information added")

    def save_file(self):
        self.workbook.save(self.file_path)
        print(self.file_name + " excel file updated")
