import openpyxl
workbook=openpyxl.load_workbook(filename='inventory.xlsx')
worksheet=workbook['Sheet1']
products_per_supplier={}

for i in range(2,worksheet.max_row+1):
    suppliername=worksheet.cell(i,4).value
    if suppliername in products_per_supplier:
        temp=products_per_supplier[suppliername]
        products_per_supplier[suppliername]=temp+1
    else:
        products_per_supplier[suppliername]=1


print(products_per_supplier)