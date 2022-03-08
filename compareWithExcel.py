import openpyxl
import  tkinter
from tkinter import simpledialog
from tkinter import messagebox

targetExcelFilePath = simpledialog.askstring("Input Box", "対象ファイルを指定して",)
comparingExcelFilePath = simpledialog.askstring("Input Box", "比較するファイルを指定して",)

targetExcelBook  = openpyxl.load_workbook(targetExcelFilePath)
targetExcelSheets = targetExcelBook.sheetnames
comparingExcelBook = openpyxl.load_workbook(comparingExcelFilePath)
comparedExcelSheets = comparingExcelBook.sheetnames

if targetExcelSheets == comparedExcelSheets:
    messagebox.showinfo('確認', '同じだから大丈夫')
else:
    messagebox.showerror('エラー', 'シートが違うから確認して')