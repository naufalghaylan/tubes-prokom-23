from csv import DictWriter


print("Selamat Datang di program admin kamera")
nama = input("Masukkan nama penyewa= ")
usia = int(input("Masukkan usia penyewa= "))
no_id = int(input("Masukkan nomer identidas penyewa= "))
alamat = input("Masukkan alamat penyewa= ")
telefon = int(input("masukkan nomor telefon penyewa= "))

penyewa_header = ['Nama', 'Usia', 'No_Identitas', 'Alamat', 'Telefon']
penyewa_data = [{'Nama' : nama, 'Usia' : usia, 'No_Identitas' : no_id, 'Alamat' : alamat, 'Telefon' : telefon}]

with open('peminjam.csv', 'a', newline='') as csv_peminjam:
    peminjam_writer = DictWriter(csv_peminjam, fieldnames=penyewa_header)
    peminjam_writer.writerows(penyewa_data)

    