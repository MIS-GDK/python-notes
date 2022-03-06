from openpyxl import workbook, load_workbook

wb = load_workbook(r"C:\Users\Administrator\Desktop\1.xlsx")
# 1、获取sheet名称
name_list = wb.sheetnames
print(name_list)

# for sheet_object in wb:
#     print(sheet_object.)
sheet = wb.worksheets[0]
sheet2 = wb.worksheets[1]
# print(sheet.rows)
row_data1 = []
all_data1 = []

row_data2 = []
all_data2 = []
# 读取数据
for row in sheet.iter_rows(min_row=1, max_row=3):
    row_data1 = [cell.value for cell in row]
    all_data1.append(row_data1)

for row in sheet2.iter_rows(min_row=1, max_row=3):
    row_data2 = [cell.value for cell in row]
    all_data2.append(row_data2)
# for row in sheet.rows:
#     print(row[0].value)
# 按行读取
# for row in sheet.iter_rows(min_row=1, max_row=3):

# 写入excel
wb2 = workbook.Workbook()
sheet3 = wb2.worksheets[0]

new_cols = len(row_data1) * 2

for row in range(1, len(all_data1) + 1):
    for col in range(1, new_cols + 1):
        # sheet3.cell(row, col).value = all_data1[row - 1][(col - 1) % 38]
        if col % 2 == 0:
            sheet3.cell(row, col).value = all_data2[row - 1][int(col / 2) - 1]
        else:
            sheet3.cell(row, col).value = all_data1[row - 1][int(col / 2)]

wb2.save(r"C:\Users\Administrator\Desktop\2.xlsx")
