class wrFile:
    def __init__(self):
        pass

    def baca_file(self, file):
        try:
            with open(file, 'r') as baca:
                return baca.read()
        except:
            print("file not found.")

    def tulis_file(self, file, teks, mode='w'):
        try:
            with open(file, mode) as tulis:
                tulis.write(teks)
                print("Teks sudah ditulis dan disimpan pada file {}.".format(file))
        except:
            print("Gagal menulis file {}.".format(file))

# menampilkan hasil program:
operasi = wrFile()
# Tulis dan membaca file
operasi.tulis_file("hasil.txt", "Ini adalah contoh teks yang ditulis ke file.\n")
print(operasi.baca_file("hasil.txt"))

