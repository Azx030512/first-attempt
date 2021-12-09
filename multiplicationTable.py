#!python3
# multiplicationTable.py -- This machine can receive an interger from the argv to create a metrx of multiplicationTable
import sys,openpyxl,logging
logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s',filename=r'C:\Users\艾\Desktop\practice\errorInfo.txt')
logging.info('Start of multiplicationTable.py')
number=int(input())+1
wb=openpyxl.Workbook()
sheet=wb.active
sheet.freeze_panes='B2'
for index in range(2,number+1):
    sheet.cell(row=1,column=index).value=index-1
    sheet.cell(column=1,row=index).value=index-1
for i in range(2,number+1):
    for j in range(2,number+1):
        sheet.cell(row=i,column=j).value=(j-1)*(i-1)
wb.save(r'C:\Users\艾\Desktop\multiplicationTable.xlsx')
logging.info('End of multiplicationTable.py,the excel has been stored to '+r'C:\Users\艾\Desktop\multiplicationTable.xlsx')
wb.close()
