import xlwings as xw
import pandas as pd
# app = xw.App(visible=True,add_book=False)
# # wb = app.books.add()
# wb = app.books.open(r'C:\Users\Administrator.user-PC\Desktop\xx\test.xls')
# wb.save()
# wb.close()
# app.quit()

# wb = xw.Book(r'C:\Users\Administrator.user-PC\Desktop\xx\test.xlsx')
# sht = wb.sheets['Sheet1']
# sht.range('A1').value = [['Foo 1', 'Foo 2', 'Foo 3'], [10.0, 20.0, 30.0]]
# print(sht.range('A1').expand().value)
# print(sht.range('A1').options(pd.DataFrame, expand='table').value)

xw.Range('A1').value = 'Foo'
