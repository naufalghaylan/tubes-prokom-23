
import csv
from datetime import date, datetime
from datetime import time
from datetime import * 

def identitas():
    global nama #global biar variabel bisa dipanggil diluar fungsi
    global usia
    global no_id
    global alamat
    global telefon
    nama = input("Masukkan Nama Penyewa\t\t\t= ")
    usia = int(input("Masukkan Usia Penyewa\t\t\t= "))
    no_id = input("Masukkan Nomer Identidas Penyewa\t= ")
    alamat = input("Masukkan Alamat Penyewa\t\t\t= ")
    telefon = int(input("Masukkan Nomor Telefon Penyewa\t\t= "))
    return (nama, usia, no_id, alamat, telefon)

def pilihkamera():
    print("===================================================")
    print("\t\t  PILIHAN KAMERA")
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
    print("Keterangan:")
    print("Harga yang tertera adalah harga per hari \n(+1) = Stok Tersedia \n(-1) = Stok Tidak Tersedia")
    print("===================================================")
    print()

def saveid():
    penyewa_header = ['Nama', 'Usia', 'No_Identitas', 'Alamat', 'Telefon']
    penyewa_data = [{'Nama' : nama, 'Usia' : usia, 'No_Identitas' : no_id, 'Alamat' : alamat, 'Telefon' : telefon}]
    with open('peminjam.csv', 'a', newline='') as csv_peminjam:
        peminjam_writer = csv.DictWriter(csv_peminjam, fieldnames=penyewa_header)
        peminjam_writer.writerows(penyewa_data)

def waktu():
    global durasi
    global tanggal
    global pengembalian
    tahun = int(input("Masukkan tahun = "))
    bulan = int(input("Masukkan bulan = "))
    tgl = int(input("Masukkan tanggal = "))
    tanggal = date(tahun, bulan, tgl)
    durasi = int(input("Masukkan durasi peminjaman = "))
    pengembalian = tanggal + timedelta(days=durasi)
    print("Tanggal Peminjaman", tanggal)
    print("Durasi Peminjaman", durasi, "Hari")
    print("Tanggal Pengembalian", pengembalian.strftime("%d %B %Y"))

def canon():
    global hargacamera
    hargacamera = durasi*5000
    print("Total Biaya = Rp",hargacamera)

def nikon():
    global hargacamera
    hargacamera = durasi*50000
    print("Total Biaya = Rp",hargacamera)

def sony():
    global hargacamera
    hargacamera = durasi*60000
    print("Total Biaya = Rp",hargacamera)

def fujifilm():
    global hargacamera
    hargacamera = durasi*75000
    print("Total Biaya = Rp",hargacamera)

def sewacam():
    kamera = input("Masukkan Kode Kamera yang Akan Disewa = ")
    if kamera == "A":
        canon()
    elif kamera == "B":
        nikon()
    elif kamera == "C":
        sony()
    else:
        fujifilm()

def payment():
    pf = [
    [1, 'Cash'],
    [2, 'E-Wallet'],
    [3, 'Transfer Bank'],
    ]
    print ()
    print("===================================================")
    print('PILIHAN PAYMENT')
    print()
 
    for i in range(0,len(pf)):
        print(pf[i][0],'\t', pf[i][1], '\t\t')
        i += 1
 
    print("===================================================")

def cash():
    print("Silakan melakukan pembayaran secara langsung dengan petugas sesuai dengan total harga")
    global metodepem
    metodepem = "Cash"

def ewallet():
    print("Silakan melakukan pembayaran melalui E-Wallet dengan nomor E-Money sebagai berikut (pilih salah satu) \nDana = 089******312 \nShopeePay = 089******312 \nOVO = 089******312 \nLink Aja = 089******312")
    global metodepem
    metodepem = "E-Wallet"

def bank():
    print("Silakan melakukan pembayaran melalui Rekening Bank dengan nomor rekening sebagai berikut (pilih salah satu) \nBNI = 98129812831 \nBRI = 812938189173 \nMandiri = 98298198719")
    global metodepem
    metodepem = "Bank"

def pilihpf():
    via = int(input("Masukkan Kode Plaftform Pembayaran = "))
    if via == 1:
        cash()
    elif via == 2:
        ewallet()
    else:
        bank()


print()
print("===================================================")
print("Selamat Datang di Program Rental Kamera untuk Admin") #yang ini tolong diedit biar apik dong dibikikin gitu lah kek biasanya program pak danu
print("===================================================")
print()
identitas()
print()
pilihkamera()
# saveid()
print("PEMINJAMAN KAMERA")
print()
waktu()
print()
sewacam()
payment()
pilihpf()

#struk
print()
print("===================================================")
print("                 STRUK PEMBELIAN") 
print("===================================================")
print("\t\tIDENTITAS PEMINJAM")
print("Nama\t\t\t=", nama)
print("Usia\t\t\t=", usia)
print("Nomer Identitas\t\t=", no_id)
print("Alamat\t\t\t=", alamat)
print("Telefon\t\t\t=", telefon)
print("Tanggal Peminjaman\t=", tanggal)
print("Durasi Peminjaman\t=", durasi, "Hari")
print("Tanggal Pengembalian\t=", pengembalian.strftime("%d %B %Y"))

print("Metode Pembayaran\t=", metodepem)
print("Total Pembayaran\t=", hargacamera)
