import sys
import os
import pandas as pd

xlFile = ''

if len(sys.argv) > 1:
    xlFile = sys.argv[1]
else:
    xlFile = r'C:/Python/TP1_python/DataPerusahaan.xlsx'

data_product = pd.read_excel(xlFile, sheet_name="Sheet1")
listJabatan = []
listGaji = []

for index, row in data_product.iterrows():
    gaji = row["Gaji"]
    listGaji.append(gaji)

    jabatan = ''
    if gaji in range(8000000, 9000001):
        jabatan = 'Officer'
    elif gaji in range(10000000, 11000001):
        jabatan = 'Supervisor'
    elif gaji in range(12000000, 14000001):
        jabatan = 'Asisten Manager'
    elif gaji >= 15000000:
        jabatan = 'Manager'
    else:
        jabatan = '-'

    listJabatan.append(jabatan)
    
data_product['Jabatan'] = listJabatan
print(data_product.head(10))

gajiTertinggi = max(listGaji)
gajiTerendah = min(listGaji)
print(f"Gaji Tertinggi: {gajiTertinggi}")
print(f"Gaji Terendah: {gajiTerendah}")

