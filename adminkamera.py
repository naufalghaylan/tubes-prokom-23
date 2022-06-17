

import csv
import fileinput
from datetime import date, datetime
from datetime import time
from datetime import *



def tak():
    if xtambahataukurang == 1:
        with open("kamera.csv", 'r') as tambah_csv:
            tambah_reader = csv.reader(tambah_csv)
            lines = list(tambah_reader)
            if lines[1][3] and lines[2][3] and lines[3][3] and lines[4][3] == "-1":
                print("")
                print("Maaf Seluruh Kamera sudah terpinjam")
                print("")
                print("Ketik 1 untuk kembali ke menu")
                print("Ketik 2 untuk keluar")
                campenuh = int(input(""))
                print("")
                if campenuh == 1:
                    campenuh = campenuh-1
                    tambahataukurang()
                    tak()
                elif campenuh == 2:
                    quit
                else:
                    print("Tolong masukkan input yang sesuai")
                    tak()
            else:
                main()
    elif xtambahataukurang == 2:
        tambahkamera()
    elif xtambahataukurang == 3:
        quit
    else:
        print("")
        print("Input tidak diterima, tolong pilih sesuai menu")
        tambahataukurang()
        tak()

def tambahataukurang():
    global xtambahataukurang
    print()
    print("===================================================")
    print("Selamat Datang di Program Rental Kamera untuk Admin") 
    print("===================================================")
    print("                    MENU PROGRAM")
    print("---------------------------------------------------")
    print("1. Program Peminjaman Kamera")
    print("2. Program Pengembalian Kamera")
    print("3. Exit")
    print("---------------------------------------------------")
    xtambahataukurang = int(input("Masukkan pilihan menu: "))

    
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


def waktu():
    global durasi
    global tanggal
    global pengembalian
    print("NOTE: Input tahun, bulan, tanggal, dan durasi dalam format angka")
    tahun = int(input("Masukkan tahun \t\t   = "))
    bulan = int(input("Masukkan bulan \t\t   = "))
    tgl = int(input("Masukkan tanggal \t   = "))
    tanggal = date(tahun, bulan, tgl)
    durasi = int(input("Masukkan durasi peminjaman = "))
    pengembalian = tanggal + timedelta(days=durasi)
    print()
    print("Tanggal Peminjaman\t", tanggal.strftime("%d %B %Y"))
    print("Durasi Peminjaman (hari)", durasi, "Hari")
    print("Tanggal Pengembalian\t", pengembalian.strftime("%d %B %Y"))


def canon():
    global hargacamera
    global cameraterpilih
    hargacamera = durasi*55000
    cameraterpilih = "Canon"
    print("Camera yang dipinjam =", cameraterpilih)
    print(f'Total Biaya = Rp. {hargacamera:,}')
def nikon():
    global hargacamera
    global cameraterpilih
    hargacamera = durasi*50000
    cameraterpilih = "Nikon"
    print("Camera yang dipinjam =", cameraterpilih)
    print(f'Total Biaya = Rp. {hargacamera:,}')
def sony():
    global hargacamera
    global cameraterpilih
    hargacamera = durasi*60000
    cameraterpilih = "Sony"
    print("Camera yang dipinjam =", cameraterpilih)
    print(f'Total Biaya = Rp. {hargacamera:,}')
def fujifilm():
    global hargacamera
    global cameraterpilih
    hargacamera = durasi*75000
    cameraterpilih = "Fujifilm"
    print("Camera yang dipinjam =", cameraterpilih)
    print(f'Total Biaya = Rp. {hargacamera:,}')

def sewacam():
    def dsewacam():
        kamera = input("Masukkan Kode Kamera yang Akan Disewa = ")
        with open("kamera.csv", 'r') as tambah_csv:
            tambah_reader = csv.reader(tambah_csv)
            lines = list(tambah_reader)
            if kamera == "A":
                if lines[1][3] == "-1":
                    print("Maaf Kamera telah dirental")
                    print("")
                    print("Ketik 1 jika ingin memilih kamera lain")
                    print("Ketik 2 jika ingin keluar dari program")
                    def dpilihlain():
                        pilihlain = int(input(">> "))
                        if pilihlain == 1:
                            print("")
                            sewacam()
                        elif pilihlain == 2:
                            quit()
                        else:
                            print("Input tidak sesuai")
                            dpilihlain()
                    dpilihlain()
                else:
                    canon()
            elif kamera == "B":
                if lines[2][3] == "-1":
                    print("Maaf Kamera telah dirental")
                    print("")
                    print("Ketik 1 jika ingin memilih kamera lain")
                    print("Ketik 2 jika ingin keluar dari program")
                    def dpilihlain():
                        pilihlain = int(input(">> "))
                        if pilihlain == 1:
                            print("")
                            sewacam()
                        elif pilihlain == 2:
                            quit()
                        else:
                            print("Input tidak sesuai")
                            dpilihlain()
                    dpilihlain()
                else:
                    nikon()
            elif kamera == "C":
                if lines[3][3] == "-1":
                    print("Maaf Kamera telah dirental")
                    print("")
                    print("Ketik 1 jika ingin memilih kamera lain")
                    print("Ketik 2 jika ingin keluar dari program")
                    def dpilihlain():
                        pilihlain = int(input(">> "))
                        if pilihlain == 1:
                            print("")
                            sewacam()
                        elif pilihlain == 2:
                            quit()
                        else:
                            print("Input tidak sesuai")
                            dpilihlain()
                    dpilihlain()
                else:
                    sony()
            elif kamera == "D":
                if lines[4][3] == "-1":
                    print("Maaf Kamera telah dirental")
                    print("")
                    print("Ketik 1 jika ingin memilih kamera lain")
                    print("Ketik 2 jika ingin keluar dari program")
                    def dpilihlain():
                        pilihlain = int(input(">> "))
                        if pilihlain == 1:
                            print("")
                            sewacam()
                        elif pilihlain == 2:
                            quit()
                        else:
                            print("Input tidak sesuai")
                            dpilihlain()
                    dpilihlain()
                else:
                    fujifilm()
            else:
                print("Input tidak sesuai")
                dsewacam()
    dsewacam()



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
    print("Silahkan melakukan pembayaran secara langsung dengan petugas sesuai dengan total harga")
    global metodepem
    metodepem = "Cash"

def ewallet():
    print("Silahkan melakukan pembayaran melalui E-Wallet dengan nomor E-Money sebagai berikut: (pilih salah satu) \nDana = 089******312 \nShopeePay = 089******312 \nOVO = 089******312 \nLink Aja = 089******312")
    global metodepem
    metodepem = "E-Wallet"

def bank():
    print("Silahkan melakukan pembayaran melalui Rekening Bank dengan nomor rekening sebagai berikut: (pilih salah satu) \nBNI = 98129812831 \nBRI = 812938189173 \nMandiri = 98298198719")
    global metodepem
    metodepem = "Bank"

def pilihpf():
    def dpilihpf():
        via = int(input("Masukkan Kode Plaftform Pembayaran = "))
        if via == 1:
            cash()
        elif via == 2:
            ewallet()
        elif via == 3:
            bank()
        else:
            print("Input tidak sesuai")
            dpilihpf()
    dpilihpf()


def saveid():
    penyewa_header = ['Nama', 'Usia', 'No_Identitas', 'Alamat', 'Telefon', 'Metode_Pembayaran', 'Kamera_Dipinjam']
    penyewa_data = [{'Nama' : nama, 'Usia' : usia, 'No_Identitas' : no_id, 'Alamat' : alamat, 'Telefon' : telefon, 'Metode_Pembayaran': metodepem, 'Kamera_Dipinjam': cameraterpilih}]
    with open('peminjam.csv', 'a', newline='') as csv_peminjam:
        peminjam_writer = csv.DictWriter(csv_peminjam, fieldnames=penyewa_header)
        peminjam_writer.writerows(penyewa_data)



with open("kamera.csv", 'r') as kurang_csv:
    kurang_reader = csv.reader(kurang_csv)
    lines = list(kurang_reader)
    def saveid_kamera():
        if cameraterpilih == "Canon":
            with open("kamera.csv", "w", newline="") as write_kurang:
                kurang_writer = csv.writer(write_kurang)
                lines[1][3] = "-1"
                lines[1][4] = tanggal
                lines[1][5] = pengembalian.strftime("%d %B %Y")
                kurang_writer.writerows(lines)
        elif cameraterpilih == "Nikon":
            with open("kamera.csv", "w", newline="") as write_kurang:
                kurang_writer = csv.writer(write_kurang)
                lines[2][3] = "-1"
                lines[2][4] = tanggal
                lines[2][5] = pengembalian.strftime("%d %B %Y")
                kurang_writer.writerows(lines)
        elif cameraterpilih == "Sony":
            with open("kamera.csv", "w", newline="") as write_kurang:
                kurang_writer = csv.writer(write_kurang)
                lines[3][3] = "-1"
                lines[3][4] = tanggal
                lines[3][5] = pengembalian.strftime("%d %B %Y")
                kurang_writer.writerows(lines)
        else:
            with open("kamera.csv", "w", newline="") as write_kurang:
                kurang_writer = csv.writer(write_kurang)
                lines[4][3] = "-1"
                lines[4][4] = tanggal
                lines[4][5] = pengembalian.strftime("%d %B %Y")
                kurang_writer.writerows(lines)

def main():
    print()
    print()
    print("===================================================")
    print("              Program Peminjaman Kamera") 
    print("===================================================")
    identitas()
    print()
    pilihkamera()
    
    print("PEMINJAMAN KAMERA")
    print()
    waktu()
    print()
    sewacam()
    payment()
    pilihpf()
    saveid_kamera()
    saveid()

    #struk
    print()
    print("===================================================")
    print("             STRUK PEMINJAMAN KAMERA") 
    print("===================================================")
    print("\t\tIDENTITAS PEMINJAM")
    print("Nama\t\t\t=", nama)
    print("Usia\t\t\t=", usia)
    print("Nomer Identitas\t\t=", no_id)
    print("Alamat\t\t\t=", alamat)
    print("Telefon\t\t\t=", telefon)
    print("Kamera\t\t\t=", cameraterpilih)
    print("Tanggal Peminjaman\t=", tanggal.strftime("%d %B %Y"))
    print("Durasi Peminjaman\t=", durasi, "Hari")
    print("Tanggal Pengembalian\t=", pengembalian.strftime("%d %B %Y"))
    print("Metode Pembayaran\t=", metodepem)
    print("Total Pembayaran\t= Rp", hargacamera)
    print("===================================================")
    def mcl():
        global cl 
        print("Apakah anda ingin memasukkan data peminjam lain? (Y/N)") 
        cl = str(input(">> "))
        if cl == "N":
            def dkmu():
                global kmu
                print("Apakah anda ingin kembali ke menu utama?(Y/N)")
                kmu = str(input(">> "))
                if kmu == "Y":
                    tambahataukurang()
                    tak()
                elif kmu == "N":
                    print("Terima kasih telah menginput data peminjam")
                    quit
                else: 
                    print("Input tidak sesuai")
                    mcl()
            dkmu()
        elif cl == "Y":
            main()
        else:
            print("Input tidak sesuai")
            mcl()
    mcl()


with open("kamera.csv", 'r') as tambah_csv:
    tambah_reader = csv.reader(tambah_csv)
    lines = list(tambah_reader)
    def tambahcanon():
        with open("kamera.csv", "w", newline="") as write_tambah:
            tambah_writer = csv.writer(write_tambah)
            lines[1][3] = "+1"
            lines[1][4] = ""
            lines[1][5] = ""
            tambah_writer.writerows(lines)
    def tambahnikon():
        with open("kamera.csv", "w", newline="") as write_tambah:
            tambah_writer = csv.writer(write_tambah)
            lines[2][3] = "+1"
            lines[2][4] = ""
            lines[2][5] = ""
            tambah_writer.writerows(lines)
    def tambahsony():
        with open("kamera.csv", "w", newline="") as write_tambah:
            tambah_writer = csv.writer(write_tambah)
            lines[3][3] = "+1"
            lines[3][4] = ""
            lines[3][5] = ""
            tambah_writer.writerows(lines)
    def tambahfujifilm():
        with open("kamera.csv", "w", newline="") as write_tambah:
            tambah_writer = csv.writer(write_tambah)
            lines[4][3] = "+1"
            lines[4][4] = ""
            lines[4][5] = ""
            tambah_writer.writerows(lines)

def tambahkamera():
    print("")
    print("===================================================")
    print("      PILIHAN KAMERA YANG AKAN DIKEMBALIKAN")
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
    def tambahpilihkamera():
        pilihantambahkamera = input(str("Masukkan kode kamera: "))
        if pilihantambahkamera == "A":
            tambahcanon()
        elif pilihantambahkamera == "B":
            tambahnikon()
        elif pilihantambahkamera == "C":
            tambahsony()
        elif pilihantambahkamera == "D":
            tambahfujifilm()
        else:
            print("Input tidak sesuai")
            tambahpilihkamera()
    tambahpilihkamera()
    print("Apakah anda ingin menambahkan stok kamera lain? (Y/N)")
    def dclk():
        global clk 
        clk = str(input(">> "))
        if clk == "Y":
            tambahkamera()
        elif clk == "N":
            def dkmu():
                global kmu
                print("Apakah anda ingin kembali ke menu utama?(Y/N)")
                kmu = str(input(">> "))
                if kmu == "Y":
                    tambahataukurang()
                    tak()
                elif kmu == "N":
                    print("Terima kasih telah menginput data kamera")
                    quit
                else:
                    print("Input tidak sesuai")
                    dkmu()
            dkmu()
        else:
            print("Input tidak sesuai")
            dclk()
    dclk()



tambahataukurang()
tak()
