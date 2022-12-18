import os
# os.system("cls")

class Mahasiswa():
    
    def __init__(self):
        self.mahasiswa = {
            "dataMahasiswa" : {
            }
            }
        

    def input(loop):
        print ("\n════════════Masukan Data Mahasiswa════════════")
        while(loop == "y"):
            while (True):
                nama = (input("NAMA    : "))
                if nama == '':
                    print ('Nama tidak boleh kosong')
                else:
                    break
            while (True):
                try:
                    nim = int(input("NIM     : "))
                    if nim == '':
                        print ('Masukan Nim dengan Angka')
                except ValueError:
                    print ('Masukan Nim dengan Angka')
                else:
                    break
            while (True):
                try:
                    tugas = int(input("TUGAS   : "))
                    if tugas == '':
                        print ('Masukan TUGAS dengan Angka')
                except ValueError:
                    print ('Masukan TUGAS dengan Angka')
                else:
                    break
            while (True):
                try:
                    uts = int(input("UTS     : "))
                    if uts == '':
                        print ('Masukan UTS dengan Angka')
                except ValueError:
                    print ('Masukan UTS dengan Angka')
                else:
                    break
            while (True):
                try:
                    uas = int(input("UAS     : "))
                    if uas == '':
                        print('Masukan UAS dengan Angka')
                except ValueError:
                    print ('Masukan UAS dengan Angka')
                else:
                    break
            akhir = round(tugas * 30 / 100) + (uts * 35 / 100) + (uas * 35 / 100)
            key = nim
            mydict.tambah(key,nama, nim, tugas, uts, uas, akhir)
            loop = input("Lanjut input data? (y/t) = ")
        while(loop == "t"):
            break

    def tambah(self, key, nama, nim, tugas, uts, uas, akhir):
        self.mahasiswa[key] = nama, nim, tugas, uts, uas, akhir

    # def get(self, key):
    #     return self.mahasiswa[key]

    def tampilkan():
        os.system("cls")
        print(mydict.mahasiswa)
        # no = 0
        # print("\n")
        # print(f"{'TABEL DATA MAHASISWA':^75}")
        # print("╭────┬──────────────────┬─────────┬───────┬───────┬───────┬───────────────╮")
        # print(f"│{'NO':^4}│{'Nama':^18}│{'NIM':^9}│{'Tugas':^7}│{'UTS':^7}│{'UAS':^7}│{'Nilai Akhir':^15}│")
        # print("├────┼──────────────────┼─────────┼───────┼───────┼───────┼───────────────┤")

        # for nim in Mahasiswa:
        #     no += 1
        #     NAMA = [0]
        #     NIM = [1]
        #     TUGAS = [2]
        #     UTS = [3]
        #     UAS = [4]
        #     AKHIR = [5]
            
        #     print(f"│{no:^4}│{NAMA:^18}│{NIM:^9}│{TUGAS:^7}│{UTS:^7}│{UAS:^7}│{AKHIR:^15}│")
        #     print("├────┼──────────────────┼─────────┼───────┼───────┼───────┼───────────────┤")

        # print("╰────┴──────────────────┴─────────┴───────┴───────┴───────┴───────────────╯")
        # print("\n")
        # input("Tekan tombol enter untuk melanjutkan")

mydict = Mahasiswa()

while True:
    # os.system("cls")
    print('{0:^46}'.format("PROGRAM INPUT NILAI MAHASISWA"))
    print('{0:^46}'.format("="*46))
    # print("\n")
    print("[(T)ambah, (U)bah, (H)apus, (L)ihat, (K)eluar]")
    pilihan = input("\nPilih Opsi= ")

    if pilihan.lower() == "t":
        Mahasiswa.input("y")
    elif pilihan.lower() == "u":
        Mahasiswa.ubah()
    elif pilihan.lower() == "h":
        Mahasiswa.hapus()
    elif pilihan.lower() == "l":
        Mahasiswa.tampilkan()
    elif pilihan.lower() == "k":
        break
    else:
        print("Opsi yang anda pilih tidak ada di menu")
        input("Tekan enter untuk melanjutkan")
