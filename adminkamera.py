
import csv
print("Selamat Datang di program admin kamera") #yang ini tolong diedit biar apik dong dibikikin gitu lah kek biasanya program pak danu

def identitas():
    global  nama #global biar variabel bisa dipanggil diluar fungsi
    global  usia
    global  no_id
    global alamat
    global telefon
    nama = input("Masukkan nama penyewa= ")
    usia = int(input("Masukkan usia penyewa= "))
    no_id = int(input("Masukkan nomer identidas penyewa= "))
    alamat = input("Masukkan alamat penyewa= ")
    telefon = int(input("masukkan nomor telefon penyewa= "))
    return (nama, usia, no_id, alamat, telefon)
identitas() 

def pilihkamera():
    print("=========================")
    print("Pilih Jenis Kamera")
    print("-------------------------")
    with open('kamera.csv', 'r', newline='') as csv_kamera:
        kamera_reader = csv.DictReader(csv_kamera)
        print("{:<10} {:<8}"
    .format("Jenis", "Harga"))
        print("")
        for line in kamera_reader:
            print("{:<10} {:<8}"
    .format(line['Jenis'], line["Harga"]))


pilihkamera()
penyewa_header = ['Nama', 'Usia', 'No_Identitas', 'Alamat', 'Telefon']
penyewa_data = [{'Nama' : nama, 'Usia' : usia, 'No_Identitas' : no_id, 'Alamat' : alamat, 'Telefon' : telefon}]
with open('peminjam.csv', 'a', newline='') as csv_peminjam:
        peminjam_writer = csv.DictWriter(csv_peminjam, fieldnames=penyewa_header)
        peminjam_writer.writerows(penyewa_data)

