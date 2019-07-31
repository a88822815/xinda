import os
import printer
path=r'D:\1'
for a,b,c in os.walk(path):
	print(c)
for i in c:
	f=os.path.join(path,i)
	if f.endswith("docx"):
		printer.printer_loading(f)
