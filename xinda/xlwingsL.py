# -*- coding: utf-8 -*-
import xlwings as xw
from openpyxl import Workbook
from openpyxl.styles import Color, Font, Alignment
import pandas as pd
import numpy as np
# app = xw.App(visible=True,add_book=False)
# wb = app.books.add()
# wb = app.books.open(r'C:\Users\Administrator.user-PC\Desktop\xx\test.xls')
# wb.save()
# wb.close()
# app.quit()

wb = xw.Book(r'C:\Users\lcy\Desktop\mama\re1.xlsx')
sht = wb.sheets[0]
line = 3

rng1 = sht.range('B3').options(np.array, expand='table')
print(type(rng1))

# sht = wb.sheets[0]
# sht.range('A1').value = [['Foo 1', 'Foo 2', 'Foo 3'], [10.0, 20.0, 30.0]]
# print(sht.range('A1').expand().value)
# print(sht.range('A1').options(pd.DataFrame, expand='table').value)

# sht.range('D1').value = '入库单'
# sht.range('B2').value = '供应商:'
# sht.range('D2').value = '日期:'
# sht.range('F2').value = '入库单号:'

# sht.range('B3:C3').merge_cells
# wb.save(r'C:\Users\lcy\Desktop\mama\pr1')

