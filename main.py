import os

os.system("cls")
mahasiswa = {}
dataMahasiswa = {}

def tambah(loop):
    os.system("cls")
    print ("\n════════════Masukan Data Mahasiswa════════════")
    no = 0
    while(loop == "y"):
        data = dict.fromkeys(mahasiswa.keys())
        while (True):
            data["nama"] = input("NAMA    : ")
            if data["nama"] == '':
                print ('Nama tidak boleh kosong')
            else:
                break
        while (True):
            try:
                data["nim"]  = int(input("NIM     : "))
                if data["nim"] == '':
                    print ('Masukan Nim dengan Angka')
            except ValueError:
                print ('Masukan Nim dengan Angka')
            else:
                break
        while (True):
            try:
                data["tugas"]  = int(input("TUGAS   : "))
                if data["tugas"] == '':
                    print ('Masukan TUGAS dengan Angka')
            except ValueError:
                print ('Masukan TUGAS dengan Angka')
            else:
                break
        while (True):
            try:
                data["uts"]  = int(input("UTS     : "))
                if data["uts"] == '':
                    print ('Masukan UTS dengan Angka')
            except ValueError:
                print ('Masukan UTS dengan Angka')
            else:
                break
        while (True):
            try:
                data["uas"]  = int(input("UAS     : "))
                if data["uas"] == '':
                    print('Masukan UAS dengan Angka')
            except ValueError:
                print ('Masukan UAS dengan Angka')
            else:
                break
        data["akhir"] = round(data["tugas"] * 30 / 100) + (data["uts"] * 35 / 100) + (data["uas"] * 35 / 100)
        KEY=data["nim"]
        dataMahasiswa.update({KEY:data})
        loop = input("Lanjut input data? (y/t) = ")
    while(loop == "t"):
        break


def tampilkan():
    os.system("cls")
    no = 0
    print("\n")
    print(f"{'TABEL DATA MAHASISWA':^75}")
    print("╭────┬──────────────────┬─────────┬───────┬───────┬───────┬───────────────╮")
    print(f"│{'NO':^4}│{'Nama':^18}│{'NIM':^9}│{'Tugas':^7}│{'UTS':^7}│{'UAS':^7}│{'Nilai Akhir':^15}│")
    print("├────┼──────────────────┼─────────┼───────┼───────┼───────┼───────────────┤")

    for data in dataMahasiswa:
        no += 1
        KEY = data

        NAMA = dataMahasiswa[KEY]['nama']
        NIM = dataMahasiswa[KEY]['nim']
        TUGAS = dataMahasiswa[KEY]['tugas']
        UTS = dataMahasiswa[KEY]['uts']
        UAS = dataMahasiswa[KEY]['uas']
        AKHIR = dataMahasiswa[KEY]['akhir']
        
        print(f"│{no:^4}│{NAMA:^18}│{NIM:^9}│{TUGAS:^7}│{UTS:^7}│{UAS:^7}│{AKHIR:^15}│")
        print("├────┼──────────────────┼─────────┼───────┼───────┼───────┼───────────────┤")

    print("╰────┴──────────────────┴─────────┴───────┴───────┴───────┴───────────────╯")
    print("\n")
    input("Tekan tombol enter untuk melanjutkan")

def hapus(nama):
    while True:
        try:    
            nims = int(input('Masukkan NIM data yang ingin di hapus : '))
        except ValueError:
                print ('Masukan NIM dengan angka')
        else:
            break    

    if nims in (dataMahasiswa.keys()):
        exekusi = input('Yakin Mau di hapus lur? (y/t) : ')
        if exekusi == 'y':
            del dataMahasiswa[nims]
        else :
            print("Data enggak jadi di hapus lur")
    else :
        print("NIM yang lu input enggak ada lur") 
        input("Tekan enter untuk melanjutkan") 


def ubah(nama):
    no = 0
    list = (dataMahasiswa.values())
    while True:
        try:    
            nims = int(input('Masukkan NIM : '))
        except ValueError:
                print ('Masukan NIM dengan angka')
        else:
            break
            
    if nims in (dataMahasiswa.keys()):

        print('Pilih data yang mau di edit')
        edit = input('[(1)nama, (2)tugas, (3)uts, (4)uas, (x)Enggak Jadi/udah ? ] = ')
        if edit == '1':
            # Belum jadi yg nim
            newNama = (input("Masukan Nama : "))
            dataMahasiswa[nims]["nama"] = newNama
        elif edit == '2' :
            newTugas = int(input("Masukan Nilai Tugas : "))
            dataMahasiswa[nims]["tugas"] = newTugas
            akhir = round(dataMahasiswa[nims]["tugas"] * 30 / 100) + (dataMahasiswa[nims]["uts"] * 35 / 100) + (dataMahasiswa[nims]["uas"] * 35 / 100)
            dataMahasiswa[nims]["akhir"] = akhir
        elif edit == '3' :
            newUts = int(input("Masukan Nilai UTS : "))
            dataMahasiswa[nims]["uts"] = newUts
            akhir = round(dataMahasiswa[nims]["tugas"] * 30 / 100) + (dataMahasiswa[nims]["uts"] * 35 / 100) + (dataMahasiswa[nims]["uas"] * 35 / 100)
            dataMahasiswa[nims]["akhir"] = akhir
        elif edit == '4' :
            newUas = int(input("Masukan Nilai Uas : "))
            dataMahasiswa[nims]["uas"] = newUas
            akhir = round(dataMahasiswa[nims]["tugas"] * 30 / 100) + (dataMahasiswa[nims]["uts"] * 35 / 100) + (dataMahasiswa[nims]["uas"] * 35 / 100)
            dataMahasiswa[nims]["akhir"] = akhir
    else:
        print("Nik lu belum ada lur")
        input("Tekan enter untuk melanjutkan")

    

while True:
    os.system("cls")
    print('{0:^46}'.format("PROGRAM INPUT NILAI MAHASISWA"))
    print('{0:^46}'.format("="*46))
    # print("\n")
    print("[(T)ambah, (U)bah, (H)apus, (L)ihat, (K)eluar]")
    pilihan = input("\nPilih Opsi= ")

    if pilihan.lower() == "t":
        tambah("y")
    elif pilihan.lower() == "u":
        ubah("ok")
    elif pilihan.lower() == "h":
        hapus('ok')
    elif pilihan.lower() == "l":
        tampilkan()
    elif pilihan.lower() == "k":
        break
    else:
        print("Opsi yang anda pilih tidak ada di menu")
        input("Tekan enter untuk melanjutkan")

