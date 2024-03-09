'''
[9 Maret 2024]

CUY-UNIVERSITY 5 - Python -- Tugas!
- Sumber: https://youtu.be/XtYprke-rpA?si=YvTHq3rXRRAOsILa
- TUGAS: Buat output dari tampilan goa tidak nampak seperti sebuah goa yang dikemas oleh list
'''

# Source code awal
'''
import random

welcome_message = 'WELCOME TO CUYPY GAMES!'
cuypy_position = random.randint(1, 4) # Memberikan bilangan bulat secara random dari nomor 1 - 4 

print(
    '*****************************\n' +
    f'** {welcome_message} **\n' + 
    '*****************************'
)

name_user = input('Masukkan nama kamu: ')

print(f'\''
    Halo {name_user}! Coba perhatikan goa di bawah ini
    |_| |_| |_| |_|
'\'')

pilihan_user = int(input('Menurut kamu di goa nomor berapa CUYPY berada? [1/2/3/4] : '))

konfirmasi_user = input(f'Apakah kamu yakin memilih {pilihan_user} ? [Y/T] :')

if konfirmasi_user.upper() == 'Y':
    print('SELAMAT KAMU MENANG!!') if pilihan_user == cuypy_position else print('Maaf kamu kalah!')
'''

# Jawaaban tugas
# Memodifikasi kode dengan memanfaatkan fungsi join()
import random

welcome_message = 'WELCOME TO CUYPY GAMES!'
cuypy_position = random.randint(1, 4) # Memberikan bilangan bulat secara random dari nomor 1 - 4 

print(
    '*****************************\n' +
    f'** {welcome_message} **\n' + 
    '*****************************'
)

name_user = input('Masukkan nama kamu: ')

# Menyiapkan goa yang akan ditebak
bentuk_goa = '|_|'
goa_kosong = [bentuk_goa] * 4

goa = goa_kosong.copy()
goa[cuypy_position - 1] = '|0_0|'

goa_baru = ' '.join(goa)


print(f'''
    Halo {name_user}! Coba perhatikan goa di bawah ini
    {' '.join(goa_kosong)}
''')

pilihan_user = int(input('Menurut kamu di goa nomor berapa CUYPY berada? [1/2/3/4] : '))

konfirmasi_user = input(f'Apakah kamu yakin memilih {pilihan_user} ? [Y/T] : ')

if konfirmasi_user.upper() == 'Y':
    if pilihan_user == cuypy_position:
        print(f'\n{goa_baru} \nSELAMAT KAMU MENANG!! 🏆') 
    else:
        print(f'\n{goa_baru} \nMaaf kamu kalah! 🙊')
elif konfirmasi_user.upper() == 'T':
    print('Program dihentikan!')
    exit()
else:
    print('Silakan ulangi programnya!')
    exit()
