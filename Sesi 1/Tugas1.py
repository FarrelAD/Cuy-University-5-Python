'''
[6 Maret 2024]

CUY-UNIVERSITY 5 - Python -- Tugas!
- Sumber: https://youtu.be/n0tURC_xeyI?si=ouX_DR2G-TIcxkiG
- TUGAS: Ketika pengguna menginputkan angka, berikan konfirmasi terlebih dahulu!
'''


# Source code awal
'''
import random

welcome_message = "WELCOME TO CUYPY GAMES!"
cuypy_position = random.randint(1, 4)

print("*****************************")
print(f"** {welcome_message} **")
print("*****************************")

nama_user = input("masukan nama kamu: ")

print(f'\''
Halo {nama_user}! Coba perhatikan goa dibawah ini  
|_| |_| |_| |_|
'\'')

pilihan_user = int(input("Menurut kamu di goa nomor berapa CUYPY berada? [1 / 2 / 3 / 4]: "))

if pilihan_user == cuypy_position:
    print("Selamat Kamu Menang!")
else:
    print("Maaf kamu kalah!")
'''

# Jawaban tugas
# Memodifikasi kode yang sudah ada dengan memberikan opsi konfirmasi pilihan
import random

welcome_message = 'WELCOME TO CUYPY GAMES!'
cuypy_position = random.randint(1, 4) # Memberikan bilangan bulat secara random dari nomor 1 - 4 

print(
    '*****************************\n' +
    f'** {welcome_message} **\n' + 
    '*****************************'
)

name_user = input('Masukkan nama kamu: ')

print(f'''
    Halo {name_user}! Coba perhatikan goa di bawah ini
    |_| |_| |_| |_|
''')

pilihan_user = int(input('Menurut kamu di goa nomor berapa CUYPY berada? [1/2/3/4] : '))

konfirmasi_user = input(f'Apakah kamu yakin memilih {pilihan_user} ? [Y/T] :')

if konfirmasi_user.upper() == 'Y':
    print('SELAMAT KAMU MENANG!!') if pilihan_user == cuypy_position else print('Maaf kamu kalah!')