### SOAL 1
# Buatlah sebuah return function dengan 1 argumen yang akan menerima inputan bilangan integer(Seconds). Dan akan menghasilkan output string dengan format waktu ("HH:MM:SS").
# HH : Hours, 2 digits, range: 00 - 99
# MM : Minutes, 2 digits, range: 00 - 59
# SS : Seconds, 2 digits, range: 00 - 59

# Case Flow: Saat dieksekusi, program akan mencetak nilai return function.
# def timeConverter(seconds):
#       .....
# Masukkan detik : 3600
# Konversi : 01:00:00

# Masukkan detik : 3665
# Konversi : 01:01:05
# Condition: Program hanya menerima angka bulat, dengan nilai maksimal 359999, jika user memasukkan nilai lebih dari 359999, bilangan desimal , bilangan negatif, maupun memasukkan string akan keluar notifikasi. Invalid Input

# Masukkan detik : ujian
# Invalid Input!

# Masukkan detik : 20.5
# Invalid Input!



#############################################
def konversidetik (masukkan_detik):
    if masukkan_detik < 359999:
        jam = int(masukkan_detik/3600)
        sisajam = int(masukkan_detik%3600)
        menit = int(sisajam/60)
        detik = int(sisajam%60)
        print(f'Konversi detik: {jam}:{menit}:{detik}')
    else:
        print('Invalid input!')

try:
    konversidetik(int(input('Masukkan detik:')))
except:
    print('Invalid input!')

##########################################################################################
### saya stuck dalam output 2 digit. yang saya kerjakan bisa hanya dapat mengeluarkan 1 digit saja
##########################################################################################