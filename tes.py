import imp


import csv
print("")
print("===================================================")
print("\t PILIHAN KAMERA YANG AKAN DIKEMBALIKAN")
print("---------------------------------------------------")
with open('kamera.csv', 'r', newline='') as csv_kamera:
    kamera_reader = csv.DictReader(csv_kamera)
    print("{:<5} {:<13} {:<11} {:<15}"
.format("Kode", "Jenis", "Harga", "Stok"))
    print("")
    for line in kamera_reader:
        print("{:<5} {:<13} {:<11} {:<15}"
.format(line['Kode'], line['Jenis'], line["Harga_per_Hari"], line['Stok']))
print("---------------------------------------------------")
print("")
pilihantambahkamera = input(str("Masukkan kode kamera"))