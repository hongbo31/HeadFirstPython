import xlrd
def readExcle():
    excleFile = xlrd.open_workbook("D:/P020180329519512192553.xls")
    excleFileSheet = excleFile.sheet_names()[0]
    sheet =excleFile.sheet_by_name("Sheet0")
    print(sheet.name,sheet.nrows,sheet.ncols)
    for row in range(1,90):
        rows = sheet.row_values(row)
        print(rows)
if __name__ == '__main__':
    readExcle()
    print("这里运行不了")





