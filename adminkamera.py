
import csv
print()
print("===================================================")
print("Selamat Datang di Program Rental Kamera untuk Admin") #yang ini tolong diedit biar apik dong dibikikin gitu lah kek biasanya program pak danu
print("===================================================")
print()

def identitas():
    global nama #global biar variabel bisa dipanggil diluar fungsi
    global usia
    global no_id
    global alamat
    global telefon
    print("IDENTITAS PEMINJAM")
    nama = input("Masukkan Nama Penyewa\t\t\t= ")
    usia = int(input("Masukkan Usia Penyewa\t\t\t= "))
    no_id = int(input("Masukkan Nomer Identidas Penyewa\t= "))
    alamat = input("Masukkan Alamat Penyewa\t\t\t= ")
    telefon = int(input("Masukkan Nomor Telefon Penyewa\t\t= "))
    return (nama, usia, no_id, alamat, telefon)
identitas() 
print()

def pilihkamera():
    print("===================================================")
    print("\t\t  PILIHAN KAMERA")
    print("---------------------------------------------------")
    with open('kamera.csv', 'r', newline='') as csv_kamera:
        kamera_reader = csv.DictReader(csv_kamera)
        print("{:<5} {:<13} {:<11}"
    .format("Kode", "Jenis", "Harga per Hari"))
        print("")
        for line in kamera_reader:
            print("{:<5} {:<13} {:<11}"
    .format(line['Kode'], line['Jenis'], line["Harga_per_Hari"]))

pilihkamera()
penyewa_header = ['Nama', 'Usia', 'No_Identitas', 'Alamat', 'Telefon']
penyewa_data = [{'Nama' : nama, 'Usia' : usia, 'No_Identitas' : no_id, 'Alamat' : alamat, 'Telefon' : telefon}]
with open('peminjam.csv', 'a', newline='') as csv_peminjam:
        peminjam_writer = csv.DictWriter(csv_peminjam, fieldnames=penyewa_header)
        peminjam_writer.writerows(penyewa_data)

        