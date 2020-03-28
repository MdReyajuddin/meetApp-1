from django.test import TestCase

import MySQLdb
import xlrd

# Create your tests here.
book = xlrd.open_workbook("pytest.xlsx")
sheet = book.sheet_by_name("source")

database = MySQLdb.connect(host="localhost", user="root", password="", db="excel")
cursor = database.cursor()

query = """ INSERT INTO site(site, cell_name, remarks, lat, long1 ,oss, area, engg, remarks1)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s) """

for r in range(1, sheet.nrows):
    site = sheet.cell(r, 0).value
    print(site)
    cell_name = sheet.cell(r, 1).value
    print(cell_name)
    remarks = sheet.cell(r, 2).value
    print(remarks)
    lat = sheet.cell(r, 3).value
    print(lat)
    long1 = sheet.cell(r, 4).value
    print(long1)
    oss = sheet.cell(r, 5).value
    print(oss)
    area = sheet.cell(r, 6).value
    print(area)
    engg = sheet.cell(r, 7).value
    print(engg)
    remarks1 = sheet.cell(r, 8).value
    print(remarks1)

    values = (site, cell_name, remarks, lat, long1 ,oss, area, engg, remarks1)
    cursor.execute(query, values)

cursor.close()
database.commit()
database.close()

print("")
print("all done")
print("")
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print("I just imported")
