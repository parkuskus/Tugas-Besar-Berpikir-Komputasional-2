''' 
Author              : Kelompok 9
Tanggal Pengerjaan  : 2-7 Desember 2024

PROGRAM ATM BANK TPB SUKSES 
Deskripsi           : Simulasi ATM (Anjungan Tunai Mandiri / Automatic Teller Machine) bahasa Indonesia dan Inggris dengan fitur-fitur berupa
                      cek saldo, penarikan tunai, transfer antarbank, pembayaran/pembelian, dan ganti pin.

KAMUS
nama_lengkap                    = menyimpan nama lengkap pengguna
tanggal_lahir                   = menyimpan tanggal lahir pengguna
status_pin                      = menyimpan status pin yang telah dimasukkan apakh benar atau tidak
pin                             = menyimpan pin dari pengguna
pin_konfirmasi                  = menyimpan pin pengguna saat mengonfirmasi pin yang telah dibuat
saldo                           = menyimpan saldo pengguna
bahasa                          = menyimpan pilihan bahasa yang dipilih pengguna
counter                         = menyimpan percobaan yang tersisa ketika pengguna salah memasukkan PIN
status_pin_masuk                = menyimpan status pin yang dimasukkan ketika pengguna akan masuk ke ATM
nama_lengkap_konfirmasi         = menyimpan nama lengkap pengguna ketika proses recovery akun
tanggal_lahir konfirmasi        = menyimpan tanggal lahir pengguna ketika recovery akun
pilihan                         = menyimpan pilihan fitur ATM yang dipilih oleh pengguna
lanjut                          = menyimpan pilihan apakah pengguna ingin melanjutkan transaksi atau tidak
tarik                           = menyimpan pilihan jumlah uang yang ingin ditarik oleh pengguna
receipt                         = menyimpan pilihan apakah pengguna ingin mencetak struk atau tidak
status_tarik                    = menyimpan status penarikan pengguna ketika memilih pilihan "5. JUMLAH LAIN" di menu penarikan tunai
cek_kode_bank                   = menyimpan pilihan pengguna apakah ingin cek kode bank atau tidak
kumpulan_bank                   = array yang menyimpan bank-bank yang tersedia
status_transfer                 = menyimpan status transfer dari pengguna
rekening_tujuan                 = menyimpan rekening tujuan 
kode_bank                       = menyimpan kode bank dari rekening tujuan
nama_penerima                   = menyimpan nama penerima dari transfer
nominal_transfer                = menyimpan nomimal yang akan ditransfer kepada rekening penerima
status_transfer                 = menyimpan pilihan pengguna apakah ingin melakukan transfer atau tidak
pilih_pembayaran                = menyimpan pilihan menu pembayaran yang ingin digunakan oleh pengguna
nomor_hp                        = menyimpan nomor telepon genggam dari pengguna
daftar_pembelian                = menyimpan nomor nomimal voucher pulsa yang dapat dipilih oleh pengguna
nominal_isi_ulang               = menyimpan nominal isi ulang yang dipilih oleh pengguna
admin_bank                      = menyimpan nomimal admin bank 
total_isi_ulang                 = menyimpan isi total biaya isi ulang pulsa yang harus dibayar pengguna
proses_transaksi                = menyimpan konfirmasi permintaan pengguna untuk membeli pulsa prabayar
nomor_meter                     = menyimpan nomor meteran listrik pengguna
id_pelanggan                    = menyimpan nomor id listrik pelanggan/pengguna
waktu                           = menyimpan waktu ketika pengguna melakukan transaksi 
status_kode                     = menyimpan pilihan pengguna apakah ingin melihat kode PAM atau tidak
nomor_pelanggan                 = menyimpan nomor PAM/Air pelanggan
tagihan                         = menyimpan tagihan yang dimiliki oleh pengguna
total_bayar                     = menyimpan total tagihan PAM yang dimiliki oleh pengguna
konfirmasi_pembayaran           = menyimpan pilihan pengguna apakah ingin melakukan pembayaran PAM atau tidak
lembar_50k                        = menyimpan jumlah lembaran 50 ribu yang ingin disetor
lembar_100k                       = menyimpan jumlah lembaran 100 ribu yang ingin disetor
setoran                         = menyimpan total uang yang akan disetor
konfirmasi_setor                = menyimpan pilihan pengguna apakah ingin melakukan setoran atau tidak

'''
import os
import time
import random
import sys
from datetime import datetime

#Subprogram
#Subprogram menampilkan menu
#Fungsi awal untuk membuat akun pengguna
def pembuatan_akun():
    #Menyambut pengguna
    print('==================================')
    print('SELAMAT DATANG DI BANK TPB SUKSES')
    print('==================================')
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

    # Membuat akun 
    print('Silahkan masukkan data-data di bawah ini!')
    nama_lengkap    = str(input('Nama Lengkap: '))
    tanggal_lahir   = str(input('Tanggal Lahir (DD/MM/YYYY): '))

    #Membuat PIN 
    status_pin = False 
    while (status_pin == False) :
        pin = str(input('Silahkan buat PIN anda: '))
        pin_konfirmasi = str(input(('Masukkan kembali PIN yang telah anda buat: '))) #Konfimasi PIN yang telah dibuat
        if (pin == pin_konfirmasi) :
            status_pin = True
        else : #Alert jika PIN yang dikonfirmasi berbeda dengan PIN yang dibuat
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('PIN yang anda masukkan belum sama. Silahkan masukkan kembali PIN anda')

    #Mengisi saldo awal
    os.system('cls' if os.name == 'nt' else 'clear')
    saldo = int(input('Masukkan jumlah saldo awal (minimum 50.000): '))
    while (saldo<50000) :
        print('Mohon maaf, saldo awal yang anda masukkan belum mencukupi batas minimal')
        saldo = int(input('Masukkan kembali saldo awal (minimum 50.000): '))

    # Menampilkan kembali data-data yang sudah dimasukkan
    os.system('cls' if os.name == 'nt' else 'clear')
    typing_effect('Berikut adalah data-data pribadi anda!')
    typing_effect(f'Nama Lengkap    : {nama_lengkap}')
    typing_effect(f'Tanggal Lahir   : {tanggal_lahir}')
    typing_effect(f'PIN             : {pin}')
    typing_effect(f'Saldo Awal      : Rp{saldo:,}'.replace(',', '.'))
    time.sleep(4)
    return pin, saldo, nama_lengkap, tanggal_lahir

#Fungsi untuk proses memasukkan kartu hingga pemilihan bahasa
def kartu_masuk():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Silakan masukkan kartu Anda untuk memulai.")
    input("Tekan Enter untuk memasukkan kartu...")

    card = [
                "|=============|",
                "|             |",
                "|             |",
                "|    KARTU    |",
                "|     ATM     |",
                "|             |",
                "|             |",
                "|=============|"
            ]

    # Cetak kartu 
    for i in range(len(card), 0, -1):
        os.system('cls' if os.name == 'nt' else 'clear')  
        for line in card[-i:]:
            print(line)
        time.sleep(0.2)
        
    os.system('cls' if os.name == 'nt' else 'clear')  
    print("Kartu berhasil dimasukkan!")
    time.sleep(2)

    #Memilih Bahasa pada ATM
    bahasa = pemilihan_bahasa()
    return bahasa

#Fungsi untuk pemilihan bahasa 
def pemilihan_bahasa():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('PILIH BAHASA YANG ANDA INGIN GUNAKAN!')
    print('1. Indonesia')
    print('2. Inggris')
    bahasa = int(input(('Pilih bahasa yang anda ingin gunakan!: ')))
    return bahasa

#last
def pin_masuk(bahasa, pin):
    if bahasa == 1:
    # Memasukkan dan Mengecek PIN yang dimasukkan
        os.system('cls' if os.name == 'nt' else 'clear')
        counter = 2
        status_pin_masuk = False
        while (counter>= 0) and (status_pin_masuk == False) :
            pin_masuk = str(input('Masukkan PIN anda: ')) 
            if (pin_masuk == pin) and (counter>0) : 
                status_pin_masuk = True
                print('Anda berhasil masuk')
            elif (counter == 0) : # Mengunci akun dan melakukan recovery akun
                os.system('cls' if os.name == 'nt' else 'clear') 
                print('Akun anda telah dikunci. Silahkan atur ulang PIN anda.')
                print('Silakan konfirmasi kembali data pribadi anda.')
                nama_lengkap_konfirmasi = str(input('Nama Lengkap: '))
                tanggal_lahir_konfirmasi = str(input('Tanggal Lahir: '))
                # Mengatur ulang PIN dengan memasukkan data-data pribadi (nama, tanggal lahir)
                if (nama_lengkap == nama_lengkap_konfirmasi) and (tanggal_lahir == tanggal_lahir_konfirmasi) :
                    status_pin = False 
                    while (status_pin == False) :
                        pin = str(input('Masukkan PIN baru anda: '))
                        pin_konfirmasi = str(input('Konfirmasikan kembali PIN anda: '))
                        if (pin == pin_konfirmasi) :
                            status_pin = True
                            print('PIN berhasil diubah!')
                            counter = 3
                        else :
                            print('PIN tidak sesuai!')

                else :# Menanyakan ulang data-data pribadi jika sebelumnya data yang diberikan di awal salah
                    while (nama_lengkap_konfirmasi != nama_lengkap) and (tanggal_lahir_konfirmasi != tanggal_lahir) :
                        print('Akun anda telah dikunci. Silahkan atur ulang PIN anda.')
                        print('Silakan konfirmasi kembali data pribadi anda.')
                        nama_lengkap_konfirmasi = str(input('Nama Lengkap: '))
                        tanggal_lahir_konfirmasi = str(input('Tanggal Lahir: '))
                    if (nama_lengkap == nama_lengkap_konfirmasi) and (tanggal_lahir == tanggal_lahir_konfirmasi) :
                        status_pin = False 
                        while (status_pin == False) :
                            os.system('cls' if os.name == 'nt' else 'clear') 
                            pin = str(input('Masukkan PIN baru anda: '))
                            pin_konfirmasi = str(input('Konfirmasikan kembali PIN anda: '))
                            if (pin == pin_konfirmasi) :
                                status_pin = True
                                print('PIN berhasil diubah!')
                                counter = 3

                                os.system('cls' if os.name == 'nt' else 'clear') 
                            else :
                                print('PIN tidak sesuai!')
                                os.system('cls' if os.name == 'nt' else 'clear') 
            else : # Alert ketika user salah memasukkkan PIN
                counter -= 1
                print(f'PIN yang dimasukkan salah. Silakan coba lagi. Anda memiliki {counter+1} kesempatan lagi')
    elif bahasa == 2:
        # Memasukkan dan Mengecek PIN yang dimasukkan
        os.system('cls' if os.name == 'nt' else 'clear')
        counter = 2
        status_pin_masuk = False
        while (counter>= 0) and (status_pin_masuk == False) :
            pin_masuk = str(input('Enter your PIN: ')) 
            if (pin_masuk == pin) and (counter>0) : 
                status_pin_masuk = True
                print('You have logged in.')
            elif (counter == 0) : # Mengunci akun dan melakukan recovery akun
                os.system('cls' if os.name == 'nt' else 'clear') 
                print('Your account has been locked. Please reset your PIN.')
                print('Please reconfirm your identity data.')
                nama_lengkap_konfirmasi = str(input('Full Name: '))
                tanggal_lahir_konfirmasi = str(input('Date Of Birth: '))
                # Mengatur ulang PIN dengan memasukkan data-data pribadi (nama, tanggal lahir)
                if (nama_lengkap == nama_lengkap_konfirmasi) and (tanggal_lahir == tanggal_lahir_konfirmasi) :
                    status_pin = False 
                    while (status_pin == False) :
                        pin = str(input('Enter your new PIN: '))
                        pin_konfirmasi = str(input('Confirm your new PIN: '))
                        if (pin == pin_konfirmasi) :
                            status_pin = True
                            print('PIN changed successfully!')
                            counter = 3
                        else :
                            print('Wrong PIN entered !')

                else :# Menanyakan ulang data-data pribadi jika sebelumnya data yang diberikan di awal salah
                    while (nama_lengkap_konfirmasi != nama_lengkap) and (tanggal_lahir_konfirmasi != tanggal_lahir) :
                        print('Your account has been locked. Please reset your PIN.')
                        print('Please reconfirm your identity data.')
                        nama_lengkap_konfirmasi = str(input('Nama Lengkap: '))
                        tanggal_lahir_konfirmasi = str(input('Tanggal Lahir: '))
                    if (nama_lengkap == nama_lengkap_konfirmasi) and (tanggal_lahir == tanggal_lahir_konfirmasi) :
                        status_pin = False 
                        while (status_pin == False) :
                            os.system('cls' if os.name == 'nt' else 'clear') 
                            pin = str(input('Enter your new PIN: '))
                            pin_konfirmasi = str(input('Confirm your new PIN: '))
                            if (pin == pin_konfirmasi) :
                                status_pin = True
                                print('PIN changed successfully!')
                                counter = 3

                                os.system('cls' if os.name == 'nt' else 'clear') 
                            else :
                                print('Wrong PIN Entered!')
                                os.system('cls' if os.name == 'nt' else 'clear') 
            else : # Alert ketika user salah memasukkkan PIN
                counter -= 1
                print(f'Wrong PIN Entered. Please try again. You have {counter+1} more chances')

    return pin

#fungsi untuk menampilkan menu transaksi yg dilakukan
def Menu(bahasa):
    if bahasa == 1: #Bahasa Indonesia
        print('SILAHKAN PILIH MENU TRANSAKSI YANG ANDA INGINKAN')
        print('1. Informasi Saldo')
        print('2. Penarikan Tunai')
        print('3. Transfer')
        print('4. Pembayaran')
        print('5. Ganti PIN')
        print('6. Setor Tunai')
        print('7. Selesai Transaksi')
        pilihan = int(input('Masukkan menu yang anda inginkan: '))
        return pilihan
    
    elif bahasa == 2: #Bahasa Inggris
        print('PLEASE SELECT YOUR DESIRED TRANSACTION MENU')
        print('1. Balance Information')
        print('2. Cash Withdrawal')
        print('3. Transfer')
        print('4. Payment')
        print('5. Change PIN')
        print('6. Cash Deposit')
        print('7. Finish Transaction')            
        pilihan = int(input('Enter your desired menu: '))
        return pilihan

#Fungsi untuk memberikan pengguna pilihan untuk melakukan transaksi kembali
def Menu_Kembali(bahasa, pilihan):
    if bahasa == 1:
        if pilihan == 1 or pilihan == 2 or pilihan == 5:
            print('Lanjut Transaksi?')
            print('1. Ya')
            print('2. Tidak')
            print('')
            lanjut = int(input('Masukkan Respon Anda: '))
            if lanjut == 1:
                pilihan = 0
            else:
                pilihan = 10
            os.system('cls' if os.name == 'nt' else 'clear') 
            return pilihan

        elif pilihan == 3 or pilihan == 4 or pilihan == 6:
            print('APAKAH ANDA MAU MELAKUKAN TRANSAKSI LAIN?')
            print('')
            status_transaksi = str(input('Konfirmasi (y/n): '))
            if (status_transaksi == 'y') :
                pilihan = 0
            else :
                pilihan = 10
            return pilihan

    elif bahasa == 2:
        if pilihan == 1 or pilihan == 2 or pilihan == 5:
            print('Continue Transaction?')
            print('1. Yes')
            print('2. No')
            print('')
            lanjut = int(input('Input Your Response Here: '))
            if lanjut == 1:
                pilihan = 0
            else:
                pilihan = 10
            os.system('cls' if os.name == 'nt' else 'clear') 
            return pilihan

        elif pilihan == 3 or pilihan == 4 or pilihan == 6:
            print('DO YOU WISH TO MAKE ANOTHER TRANSACTION?')
            print('')
            status_transaksi = str(input('Confirmation (y/n): '))
            if (status_transaksi == 'y') :
                pilihan = 0
            else :
                pilihan = 10
            return pilihan

#Fungsi untuk mengonfirmasi pencetakan receipt
def receipt_konfirmasi(bahasa, saldo, tunai):
    if bahasa == 1:
        os.system('cls' if os.name == 'nt' else 'clear')  
        print('HARAP MENUNGGU')
        print('TRANSAKSI ANDA SEDANG DIPROSES')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')   
        saldo -= tunai  
        print(f'Anda telah berhasil menarik Rp {tunai:,}'.replace(',', '.'))
        print(f'Sisa saldo di rekening anda adalah Rp {saldo:,}'.replace(',', '.'))
        print('')
        print('Apakah anda ingin mencetak receipt?')
        print('1. Ya')
        print('2. Tidak')
        receipt = int(input())
        os.system('cls' if os.name == 'nt' else 'clear') 
        return saldo, receipt

    elif bahasa == 2:
        os.system('cls' if os.name == 'nt' else 'clear')  
        print('PLEASE WAIT')
        print('YOUR TRANSACTION IS BEING PROCESSED')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')   
        saldo -= tunai  
        print(f'You have successfully withdrawedt Rp {tunai:,}'.replace(',', '.'))
        print(f'Your remaining account balance is Rp{saldo:,}'.replace(',', '.'))
        print('Do you wish to print the receipt?')
        print('1. Yes')
        print('2. No')
        receipt = int(input('Input Your Response Here: '))
        os.system('cls' if os.name == 'nt' else 'clear') 
        return saldo, receipt

#Fungsi untuk mencetak receipt
def receipt_cetak(bahasa, tunai, saldo):
    if bahasa == 1:
        waktu = datetime.now().isoformat(' ', 'seconds')
        print('---------------------------------------------------')
        print('TARIK TUNAI')
        print(f'JUMLAH            : Rp{tunai:,}'.replace(',', '.'))
        print(f'SISA SALDO        : Rp{saldo:,}'.replace(',', '.'))
        print(f'WAKTU TRANSAKSI   : {waktu}')
        print('---------------------------------------------------')
        return

    elif bahasa == 2:
        waktu = datetime.now().isoformat(' ', 'seconds')
        print('---------------------------------------------------')
        print('CASH WITHDRAWAL')
        print(f'TOTAL                  : Rp{tunai:,}'.replace(',', '.'))
        print(f'REMAINING BALANCE      : Rp{saldo:,}'.replace(',', '.'))
        print(f'TRANSACTION TIME       : {waktu}')
        print('---------------------------------------------------')
        return

#Fungsi untuk melakukan menu Cek Saldo
def cek_Saldo(bahasa, saldo, pilihan):
    if bahasa == 1: #Bahasa Indonesia
        print('HARAP MENUNGGU')
        print('TRANSAKSI ANDA SEDANG DIPROSES')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')   

        # Menampilkan saldo rekening         
        print('SALDO REKENING ANDA')
        print(f'RP.{saldo:,}'.replace(',', '.'))
        print('')
            
        # Konfirmasi lanjut transaksi/tidak?
        pilihan = Menu_Kembali(bahasa, pilihan)
        return pilihan
    
    elif bahasa == 2: #Bahasa Inggris
        print('PLEASE WAIT')
        print('YOUR TRANSACTION IS BEING PROCESSED')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')   

        # Menampilkan saldo rekening         
        print('YOUR ACCOUNT BALANCE')
        print(f'RP.{saldo:,}'.replace(',', '.'))
        print('')
        
        # Konfirmasi lanjut transaksi/tidak?
        lanjut = Menu_Kembali(bahasa, pilihan)
        return lanjut  

#Fungsi untuk melakukan penarikan tunai
def penarikan_tunai(bahasa, saldo, pilihan):
    if bahasa == 1:
        Menu_Penarikan = [0, 50000, 200000, 500000, 1000000] #Array nominal penarikan
        tarik = tarik_pilih(bahasa)
            
        # Penarikan Tunai Cepat
        if tarik == 1 or tarik == 2 or tarik == 3 or tarik == 4:
            receipt, tunai, saldo = tarik_Tunai(bahasa, saldo, tarik, Menu_Penarikan)
                        
    # Mengambil selain pilihan sebelumnya (harus kelipatan 50.000, maks Rp1.250.000)         
        elif tarik == 5:
            status_tarik = False
            while status_tarik == False:   
                tunai = tunai_5(bahasa)
                status_tarik = tarik_konfirmasi(bahasa, tunai)

            # Mencetak sisa saldo setelah tarik tunai
            if status_tarik == True:
                saldo, receipt = receipt_konfirmasi(bahasa, saldo, tunai)

        # Mencetak receipt
        if receipt == 1:
            receipt_cetak(bahasa, tunai, saldo)
                
        # Ingin lanjut bertransaksi?
        pilihan = Menu_Kembali(bahasa, pilihan)
        return pilihan, saldo

    elif bahasa == 2:
        Menu_Penarikan = [0, 50000, 200000, 500000, 1000000]
        tarik = tarik_pilih(bahasa)
            
        # Penarikan Tunai Cepat
        if tarik == 1 or tarik == 2 or tarik == 3 or tarik == 4:
            receipt, tunai, saldo = tarik_Tunai(bahasa, saldo, tarik, Menu_Penarikan)
            
        # Mengambil selain pilihan sebelumnya (harus kelipatan 50.000, maks Rp1.250.000)         
        elif tarik == 5:
            status_tarik = False
            while status_tarik == False:   
                tunai = tunai_5(bahasa)
                status_tarik = tarik_konfirmasi(bahasa, tunai)
                
                # Mencetak sisa saldo setelah tarik tunai
                if status_tarik == True:
                    saldo, receipt = receipt_konfirmasi(bahasa, saldo, tunai)

        # Mencetak receipt
        if receipt == 1:
            receipt_cetak(bahasa, tunai, saldo)
                
        # Ingin lanjut bertransaksi?
        pilihan = Menu_Kembali(bahasa, pilihan) 
        return pilihan, saldo

#Fungsi untuk memilih banyak uang yang akan di tarik
def tarik_pilih(bahasa):
    if bahasa == 1:
        print('MENU PENARIKAN CEPAT')
        print('SILAKAN PILIH JUMLAH PENARIKAN')
        print('1. Rp    50.000')
        print('2. Rp   200.000')
        print('3. Rp   500.000')
        print('4. Rp 1.000.000')
        print('5. JUMLAH LAIN')
        print('')
        tarik = int(input('Masukkan Respon Anda: '))
        os.system('cls' if os.name == 'nt' else 'clear')
        return tarik

    elif bahasa == 2:
        print('FAST WITHDRAWAL MENU')
        print('PLEASE ENTER WITHDRAWAL AMOUNT')
        print('1. Rp    50.000')
        print('2. Rp   200.000')
        print('3. Rp   500.000')
        print('4. Rp 1.000.000')
        print('5. OTHER AMOUNT')
        tarik = int(input('Input Your Response Here: '))
        os.system('cls' if os.name == 'nt' else 'clear')
        return tarik

#Fungsi untuk menarik tunai selain pilihan yang tersedia
def tarik_Tunai(bahasa, saldo, tarik, nominal):
    if bahasa == 1:
        receipt = 0
        tunai = 0
        print('HARAP MENUNGGU')
        print('TRANSAKSI ANDA SEDANG DIPROSES')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        if saldo >= nominal[tarik]:
            saldo -= nominal[tarik]
            tunai = nominal[tarik]
            print(f'Anda telah berhasil menarik Rp{nominal[tarik]:,}'.replace(',','.'))
            print(f'Sisa saldo di rekening anda adalah Rp{saldo:,}'.replace(',', '.'))
            print('Apakah anda ingin mencetak receipt?')
            print('1. Ya')
            print('2. Tidak')
            print('')
            receipt = int(input('Masukkan Respon Anda: '))
            return receipt, tunai, saldo
        else:
            print('SALDO TIDAK MENCUKUPI')
            print('')   
            return receipt, tunai,saldo

    elif bahasa == 2:
        receipt = 0
        tunai = 0
        print('PLEASE WAIT')
        print('YOUR TRANSACTION IS BEING PROCESSED')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear') 
        if saldo >= nominal[tarik]:
            saldo -= nominal[tarik]
            tunai = nominal[tarik]
            print(f'You have successfully withdrawed Rp{nominal[tarik]:,}'.replace(',','.'))
            print(f'Your remaining account balance is Rp{saldo:,}'.replace(',', '.'))
            print('Do you wish to print the receipt?')
            print('1. Yes')
            print('2. No')
            receipt = int(input('Input Your Response Here: '))
            return receipt, tunai, saldo
        else:
            print('BALANCE NOT ENOUGH')
            print('')     
            return receipt, tunai, saldo

def tunai_5(bahasa):
    if bahasa == 1:
        print('MASUKKAN JUMLAH PENARIKAN TUNAI YANG ANDA INGINKAN')
        print('(DALAM KELIPATAN RP50.000)')
        print('MAKSIMAL RP1.250.000')
        tunai = int(input('JUMLAH PENARIKAN: '))
        return tunai

    elif bahasa == 2:
        print('ENTER YOUR DESIRED CASH AMOUNT')
        print('(MULTIPLE OF RP50.000)')
        print('MAXIMAL RP1.250.000')
        tunai = int(input('JUMLAH PENARIKAN: '))
        return tunai

def tarik_konfirmasi(bahasa, tunai):
    if bahasa == 1:
        if tunai < 50000:
            print('NOMINAL YANG DIINPUT TIDAK MENCUKUPI')
            print('')
        elif tunai > 1250000:
            print('NOMINAL YANG DIINPUT TERLALU BESAR')
            print('')
        elif tunai % 50000 != 0:
            print('NOMINAL TIDAK VALID')
            print('')
        elif saldo < tunai:
            print('SALDO TIDAK MENCUKUPI')
            print('')
        else: 
            print(f'NOMINAL YANG ANDA INPUT ADALAH Rp{tunai:,}'.replace(',', '.'))
            print('APAKAH ANDA YAKIN?')
            print('')
            konfirmasi_tarik = input('Konfirmasi (y/n): ')
            if konfirmasi_tarik == 'y':
                status_tarik = True
        return status_tarik
    
    elif bahasa == 2:
        if tunai < 50000:
            print('AMOUNT TOO SMALL')
            print('')
        elif tunai > 1250000:
            print('AMOUNT TOO LARGE')
            print('')
        elif tunai % 50000 != 0:
            print('AMOUNT INVALID')
            print('')
        elif saldo < tunai:
            print('BALANCE NOT ENOUGH')
            print('')
        else: 
            print(f'THE AMOUNT YOU INPUTTED IS Rp{tunai:,}'.replace(',', '.'))
            print('ARE YOU SURE?')
            konfirmasi_tarik = input('Confirmation (y/n): ')
            if konfirmasi_tarik == 'y':
                status_tarik = True
        
        return status_tarik

def transfer_bank(bahasa, saldo, pilihan):
    kumpulan_bank, status_transfer = bank_code(bahasa)
    # Memasukkan nomor rekening tujuan
    while (status_transfer == 'n'):
        status_transfer, nominal_transfer, kode_bank, rekening_tujuan, nama_penerima = proses_transfer(bahasa, saldo, kumpulan_bank)

        os.system('cls' if os.name == 'nt' else 'clear') 
        if (status_transfer == 'y') :
            pilihan, saldo = struk_transfer(bahasa, saldo, nominal_transfer, kumpulan_bank, kode_bank, rekening_tujuan, nama_penerima, pilihan)
    return pilihan, saldo

def bank_code(bahasa):
    kumpulan_bank = {
                '001':'BRI',        '007' : 'MANDIRI',
                '002':'BNI',        '008' : 'BTN',
                '003':'BRI',        '009' : 'PERMATA',
                '004':'RBS',        '010' : 'DKI',
                '005':'CITIBANK',   '011' : 'BSI',
                '006':'MUAMALAT',   '012' : 'KB BUKOPIN',
            }

    status_transfer = 'n'

    if bahasa == 1:
        print('===================ATM TRANSFER===================')
        print('==============MASUKKAN KODE BANK DAN==============')
        print('============NOMOR REKENING TUJUAN ANDA============')
        typing_effect('No. Kode Bank Yang Tersedia Diikuti Oleh No. Rek Tujuan')
        typing_effect('3 nomor diawal kode bank diikuti dengan 5 nomor rekening bank')
        typing_effect('Cth. 42612345')
        print('')

        print('Apakah anda ingin melihat kode bank terlebih dahulu (y/n)?')
        cek_kode_bank = str(input('Masukkan Respon Anda: '))

        # Mencetak daftar kode bank
        os.system('cls' if os.name == 'nt' else 'clear') 
        if (cek_kode_bank == 'y') :
            print('DAFTAR KODE BANK')
            print('001: BRI             007: MANDIRI')
            print('002: BNI             008: BTN')
            print('003: BCA             009: PERMATA')
            print('004: RBS             010: DKI')
            print('005: CITIBANK        011: BSI')
            print('006: MUAMALAT        012: KB BUKOPIN')

            time.sleep(7)
            print('Transaksi Akan Dilanjutkan')

            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

            print('=================ATM TRANSFER=================')
            print('MASUKKAN KODE BANK DAN')
            print('NOMOR REKENING TUJUAN')
            typing_effect('No. Kode Bank Diikuti Oleh No. Rek Tujuan')
            typing_effect('3 nomor diawal kode bank diikuti dengan 5 nomor rekening bank')
            typing_effect('Cth. 00112345')
            print('')
            print('')

        return kumpulan_bank, status_transfer

    elif bahasa == 2:
        print('-----------------ATM TRANSFER---------------------')
        print('------------ENTER YOUR BANK CODE AND--------------')
        print('---------THE DESTINATION ACCOUNT NUMBER-----------')
        typing_effect('Bank Code Followed By Destination Account Number')
        typing_effect(' 3 digits bank code followed by 5 digits destination account')
        typing_effect('Cth. 42612345')

        print('Do you wish to see the bank codes first? (y/n)?')
        cek_kode_bank = str(input('Input Your Response Here: '))

            # Mencetak daftar kode bank
        os.system('cls' if os.name == 'nt' else 'clear') 
        if (cek_kode_bank == 'y') :
            print('BANK CODES LIST')
            print('001: BRI             007: MANDIRI')
            print('002: BNI             008: BTN')
            print('003: BCA             009: PERMATA')
            print('004: RBS             010: DKI')
            print('005: CITIBANK        011: BSI')
            print('006: MUAMALAT        012: KB BUKOPIN')

        time.sleep(7)
        print('Transaksi Akan Dilanjutkan')

        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

        print('-----------------ATM TRANSFER---------------------')
        print('------------ENTER YOUR BANK CODE AND--------------')
        print('---------THE DESTINATION ACCOUNT NUMBER-----------')
        typing_effect('Bank Code Followed By Destination Account Number')
        typing_effect(' 3 digits bank code followed by 5 digits destination account')
        typing_effect('Cth. 42612345')
        print('')
        print('')

        return kumpulan_bank, status_transfer

def proses_transfer(bahasa ,saldo, kumpulan_bank):
    if bahasa == 1:
        rekening_tujuan = str(input('Nomor Rekening Tujuan: '))
        kode_bank = rekening_tujuan[:3]
        nama_penerima = str(input('Nama Penerima: '))
        nominal_transfer = int(input('Masukkan Jumlah Nominal Yang  Akan Ditransfer: '))
        while (nominal_transfer>saldo) :
            print('MOHON MAAF, SALDO ANDA TIDAK MENCUKUPI')
            nominal_transfer = int(input('Masukkan Kembali Nominal Yang Akan Ditransfer: '))

        print('HARAP MENUNGGU')
        print('TRANSAKSI ANDA SEDANG DIPROSES')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')   
                
        # Konfirmasi data transfer
        print('---------------------------------------------------')
        print('TRANSFER ATM')
        print(f'Bank            : {kumpulan_bank[kode_bank]}')
        print(f'Tujuan          : {rekening_tujuan}')
        print(f'Penerima        : {nama_penerima}')
        print(f'Jumlah Transfer : Rp{nominal_transfer:,}'.replace(',', '.'))
        print('---------------------------------------------------')

        status_transfer = str(input('Apakah data sudah sesuai (y/n)? '))
        return status_transfer, nominal_transfer, kode_bank, rekening_tujuan, nama_penerima

    elif bahasa == 2:
        rekening_tujuan = str(input('Destination Account Number: '))
        kode_bank = rekening_tujuan[:3]
        nama_penerima = str(input('Transferee Name: '))
        nominal_transfer = int(input('Enter The Amount You Wish To Transfer: '))
        while (nominal_transfer>saldo) :
            print('SORRY, YOUR BALANCE IS NOT ENOUGH')
            nominal_transfer = int(input('Renter The Amount You Wish To Transfer: '))

        print('PLEASE WAIT')
        print('YOUR TRANSACTION IS BEING PROCESSED')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')   
                
        # Konfirmasi data transfer
        print('---------------------------------------------------')
        print('TRANSFER ATM')
        print(f'Bank            : {kumpulan_bank[kode_bank]}')
        print(f'Destination     : {rekening_tujuan}')
        print(f'Transferee      : {nama_penerima}')
        print(f'Transfer Amount : Rp{nominal_transfer:,}'.replace(',', '.'))
        print('---------------------------------------------------')

        status_transfer= str(input(('Is the data correct (y/n)? ')))
        return status_transfer, nominal_transfer, kode_bank, rekening_tujuan, nama_penerima

def struk_transfer(bahasa, saldo, nominal_transfer, kumpulan_bank, kode_bank, rekening_tujuan, nama_penerima, pilihan):
    if bahasa == 1:
        print('HARAP MENUNGGU')
        print('TRANSAKSI ANDA SEDANG DIPROSES')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')   
        waktu = datetime.now().isoformat(' ', 'seconds')
        saldo -= nominal_transfer

        # Mencetak struk transfer
        print('------------------------------------------------------')
        typing_effect('TRANSFER ATM')
        typing_effect(f'Bank            : {kumpulan_bank[kode_bank]}')
        typing_effect(f'Tujuan          : {rekening_tujuan}')
        typing_effect(f'Penerima        : {nama_penerima}')
        typing_effect(f'Jumlah Transfer : Rp{nominal_transfer:,}'.replace(',', '.'))
        typing_effect(f'Waktu Transaksi : {waktu}')
        print('------------------------------------------------------')
        print('')
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')   

        print('TRANSAKSI TELAH SELESAI')
        pilihan = Menu_Kembali(bahasa, pilihan)
        return pilihan, saldo

    elif bahasa == 2:
        print('PLEASE WAIT')
        print('YOUR TRANSACTION IS BEING PROCESSED')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')   
        waktu = datetime.now().isoformat(' ', 'seconds')
        saldo -= nominal_transfer

        # Mencetak struk transfer
        print('------------------------------------------------------')
        typing_effect('TRANSFER ATM')
        typing_effect(f'Bank              : {kumpulan_bank[kode_bank]}')
        typing_effect(f'Destination       : {rekening_tujuan}')
        typing_effect(f'Transferee        : {nama_penerima}')
        typing_effect(f'Transfer Amount   : Rp{nominal_transfer:,}'.replace(',', '.'))
        typing_effect(f'Transaction Time  : {waktu}')
        print('------------------------------------------------------')
        print('')
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')   

        print('TRANSAKSI TELAH SELESAI')
        pilihan = Menu_Kembali(bahasa, pilihan)
        return pilihan, saldo

def pembayaran(bahasa, saldo, nama_lengkap, pilihan):
    pilih_pembayaran = bayar_pilih(bahasa) 

    # Pembayaran telepon/HP
    if (pilih_pembayaran == 1) :
        pilihan, saldo = bayar_1(bahasa, pilihan, saldo)

    # Pembayaran PLN
    elif (pilih_pembayaran == 2) :
        pilihan, saldo = bayar_2(bahasa, saldo, nama_lengkap, pilihan)

    # Menu pembayaran PDAM
    elif (pilih_pembayaran == 3) :
        pilihan, saldo = bayar_3(bahasa, saldo, nama_lengkap, pilihan)

    return pilihan, saldo

def bayar_pilih(bahasa):
    if bahasa == 1:
        print('----------------------SILAHKAN PILIH----------------------')
        print('---------------JENIS PEMBAYARAN/PEMBELIAN-----------------')
        print('1. Telepon/HP')
        print('2. Listrik/PLN')
        print('3. Air/PDAM')
        print('')
        pilih_pembayaran = int(input('Masukkan Respon Anda: '))
        os.system('cls' if os.name == 'nt' else 'clear') 
        
    elif bahasa == 2:
        print('----------------------PLEASE CHOOSE ----------------------')
        print('---------------PAYMENT / PURCHASE TYPE--------------------')
        print('1. Telephone')
        print('2. Electric Bill/PLN')
        print('3. Water Bill/PDAM')
        print('')
        pilih_pembayaran = int(input('Input Your Response Here: '))
        os.system('cls' if os.name == 'nt' else 'clear')
    
    return pilih_pembayaran

def bayar_1 (bahasa, pilihan, saldo):
    nomor_hp, daftar_pembelian, nominal_isi_ulang, total_isi_ulang, proses_transaksi =  data_bayar_1(bahasa)
    # Pemrosesan transaksi
    if (proses_transaksi == 'y') and (saldo>=total_isi_ulang) :

        pilihan, saldo = proses_bayar_1(pilihan, bahasa, saldo, nomor_hp, daftar_pembelian, nominal_isi_ulang, total_isi_ulang)

    # Kondisi ketika saldo tidak mencukupi
    elif (proses_transaksi == 'y') and (saldo<total_isi_ulang) :
        if bahasa == 1:
            print('MOHON MAAF SALDO ANDA TIDAK MENCUKUPI')

        elif bahasa == 2:
            print('SORRY YOUR BALANCE IS NOT ENOUGH')

        pilihan = Menu_Kembali(bahasa, pilihan)

    # Kembali ke menu utama
    else :
        if bahasa == 1:
            print('MOHON TUNGGU SEBENTAR')
            print('ANDA AKAN DIALIHKAN KE MENU UTAMA')
        
        elif bahasa == 2:
            print('PLEASE WAIT A MOMENT')
            print('YOU WILL BE REDIRECTED TO THE MAIN MENU')

        time.sleep(1)
        pilihan = 0

    return pilihan, saldo

def data_bayar_1(bahasa):
    daftar_pembelian = {
                    '1' : 20000,            '5' : 150000,
                    '2' : 25000,            '6' : 200000,
                    '3' : 50000,            '7' : 300000,
                    '4' : 100000,           
                }
    if bahasa == 1:
        print('SILAHKAN MASUKKAN')
        print('NOMOR PELANGGAN/NOMOR')
        print('TAGIHAN/KODE PEMBAYARAN/NOMOR HANDPHONE ANDA')
        print('')
        nomor_hp = str(input('Nomor Telepon: '))
        os.system('cls' if os.name == 'nt' else 'clear')   

        print('HARAP MENUNGGU')
        print('TRANSAKSI ANDA SEDANG DIPROSES')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')   
        
        # Mencetak nominal transfer
        print('PILIH JUMLAH NOMIMAL')
        print('1. 20.000            5. 150.000')
        print('2. 25.000            6. 200.000')
        print('3. 50.000            7. 300.000')
        print('4. 100.000')
        print('')

        nominal_isi_ulang = str(input('Pilih nominal isi ulang anda: '))
        admin_bank = 1000
        total_isi_ulang = daftar_pembelian[nominal_isi_ulang] + admin_bank

        # Konfirmasi sebelum transaksi
        os.system('cls' if os.name == 'nt' else 'clear')   
        print('-------------------PEMBELIAN PULSA PRABAYAR-------------------')
        print(f'Nomor Handphone     : {nomor_hp}')
        print(f'Jumlah              : {daftar_pembelian[nominal_isi_ulang]:,}'.replace(',', '.'))
        print(f'TOTAL               : {total_isi_ulang:,}'.replace(',', '.'))
        print('')
        print('PROSES TRANSAKSI (y/n)? ')
        proses_transaksi = str(input('Masukkan Respon Anda: '))
        os.system('cls' if os.name == 'nt' else 'clear')  

    

    elif bahasa == 2:
        print('PLEASE ENTER')
        print('CUSTOMER CODE/ INVOICE')
        print('NUMBER/PAYMENT CODE/PHONE NUMBER')
        print('')
        nomor_hp = str(input('Insert your phone number: '))
        os.system('cls' if os.name == 'nt' else 'clear')   

        print('PLEASE WAIT')
        print('YOUR TRANSACTION IS BEING PROCESSED')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')   

        daftar_pembelian = {
            '1' : 20000,            '5' : 150000,
            '2' : 25000,            '6' : 200000,
            '3' : 50000,            '7' : 300000,
            '4' : 100000,           
        }

        # Mencetak nominal transfer
        print('CHOOSE AMOUNT')
        print('1. 20.000            5. 150.000')
        print('2. 25.000            6. 200.000')
        print('3. 50.000            7. 300.000')
        print('4. 100.000')
        print('')

        nominal_isi_ulang = str(input(''))
        admin_bank = 1000
        total_isi_ulang = daftar_pembelian[nominal_isi_ulang] + admin_bank

        # Konfirmasi sebelum transaksi
        os.system('cls' if os.name == 'nt' else 'clear')   
        print('-----------------PREPAID PHONE CREDIT PURCHASE-----------------')
        print(f'PHONE NUMBER        : {nomor_hp}')
        print(f'CREDIT AMOUNT       : {daftar_pembelian[nominal_isi_ulang]:,}'.replace(',', '.'))
        print(f'TOTAL               : {total_isi_ulang:,}'.replace(',', '.'))
        print('')
        print('CONFIRM TRANSACTION (y/n)? ')
        proses_transaksi = str(input('Input Your Response Here: '))
        os.system('cls' if os.name == 'nt' else 'clear')   

    return nomor_hp, daftar_pembelian, nominal_isi_ulang, total_isi_ulang, proses_transaksi

def proses_bayar_1(pilihan, bahasa, saldo, nomor_hp, daftar_pembelian, nominal_isi_ulang, total_isi_ulang):
    if bahasa == 1:
        saldo -= total_isi_ulang
        print('HARAP MENUNGGU')
        print('TRANSAKSI ANDA SEDANG DIPROSES')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')   

        print('TRANSAKSI BERHASIL')
        print('BERIKUT ADALAH STRUK ANDA')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear') 
        
        # Mencetak struk transaksi pembayaran telepon/HP
        print('---------------------BANK TPB SUKSES----------------------')
        print('-----------------PEMBELIAN PULSA PRABAYAR-----------------')
        waktu = datetime.now().isoformat(' ', 'seconds')
        typing_effect(f'Nomor Handphone     : {nomor_hp}')
        typing_effect(f'Voucher Reff        : {random.randint(10000000000,99999999999)}')
        typing_effect(f'Jumlah              : {daftar_pembelian[nominal_isi_ulang]:,}'.replace(',', '.'))
        typing_effect(f'TOTAL               : {total_isi_ulang:,}'.replace(',', '.'))
        typing_effect(f'Waktu Transaksi     : {waktu}')
        print('---------Jl. Let. Jend. Purn. Dr. (HC) Mashudi No.1-------')
        print('-----------PROVIDER BERKOM MENYATAKAN STRUK INI-----------')
        print('-------------SEBAGAI BUKTI PEMBAYARAN YANG SAH------------')
        print('')

        pilihan = Menu_Kembali(bahasa, pilihan)
        

    elif bahasa == 2:
        saldo -= total_isi_ulang
        print('PLEASE WAIT')
        print('YOUR TRANSACTION IS BEING PROCESSED')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')   

        print('TRANSACTION SUCCESS')
        print('HERE IS YOUR RECEIPT')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear') 
        
        # Mencetak struk transaksi pembayaran telepon/HP
        print('---------------------BANK TPB SUKSES----------------------')
        print('--------------PREPAID PHONE CREDIT PURCHASE---------------')
        waktu = datetime.now().isoformat(' ', 'seconds')
        print('')
        typing_effect(f'Phone Number        : {nomor_hp}')
        typing_effect(f'Voucher Reff        : {random.randint(10000000000,99999999999)}')
        typing_effect(f'Credit Amount       : {daftar_pembelian[nominal_isi_ulang]:,}'.replace(',', '.'))
        typing_effect(f'TOTAL               : {total_isi_ulang:,}'.replace(',', '.'))
        typing_effect(f'Transaction Time    : {waktu}')
        print('')
        print('---------Jl. Let. Jend. Purn. Dr. (HC) Mashudi No.1-------')
        print('----------PROVIDER BERKOM DECLARES THIS RECEIPT-----------')
        print('----------------AS VALID PROOF OF PURCHASE----------------')
        print('')

        pilihan = Menu_Kembali(bahasa, pilihan)

    return pilihan, saldo  
    
def bayar_2(bahasa, saldo, nama_lengkap, pilihan):
    # Meminta data untuk melakukan pembayaran
    nomor_meter, id_pelanggan = data_bayar_2(bahasa, nama_lengkap)

    # Memilih nominal isi ulang
    nominal_isi_ulang, admin_bank, total_isi_ulang, daftar_pembelian = nominal_bayar_2(bahasa)
    
    # Kondisi ketika saldo mencukupi 
    if (saldo>=total_isi_ulang) :
        saldo = proses_bayar_2(bahasa, saldo, nama_lengkap, nomor_meter, id_pelanggan, daftar_pembelian, total_isi_ulang, nominal_isi_ulang, admin_bank)

        pilihan = Menu_Kembali(bahasa, pilihan) 
    
    # Kondisi ketika saldo tidak mencukupi
    else :
        if bahasa == 1:
            print('MOHON MAAF SALDO ANDA TIDAK MENCUKUPI')
        elif bahasa == 2:
            print('SORRY YOUR BALANCE IS NOT ENOUGH')

        pilihan = Menu_Kembali(bahasa, pilihan)
        
    return pilihan, saldo

def data_bayar_2(bahasa, nama_lengkap):
    if bahasa == 1:
        print('MASUKKAN NOMOR METER ANDA')
        nomor_meter     = int(input(''))
        id_pelanggan    = random.randint(100000000000,999999999999)

        print('HARAP TUNGGU')
        print('TRANSAKSI ANDA SEDANG DIPROSES')
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')   

        # Menampilkan data listrik user
        print('---------------PEMBELIAN LISTRIK PRABAYAR---------------')
        print(f'Nomor Meter         : {nomor_meter}')
        print(f'IDPEL               : {id_pelanggan}')
        print(f'Nama                : {nama_lengkap}')
        print(f'Tarif/Daya          : R1M / 900 VA')
        print()
 
    elif bahasa == 2:
        print('ENTER YOUR METER NUMBER')
        nomor_meter     = int(input(''))
        id_pelanggan    = random.randint(100000000000,999999999999)

        print('PLEASE WAIT')
        print('YOUR TRANSACTION IS BEING PROCESSED')
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')   

        # Menampilkan data listrik user
        print('-----------------PREPAID ELECTRIC PAYMENT-----------------')
        print(f'Meter Number        : {nomor_meter}')
        print(f'Customer ID         : {id_pelanggan}')
        print(f'Name                : {nama_lengkap}')
        print(f'Tariff/Power        : R1M / 900 VA')
        print()
        
    return nomor_meter, id_pelanggan

def nominal_bayar_2(bahasa):
    daftar_pembelian = {
                    '1' : 20000,            '5' : 500000,
                    '2' : 50000,            '6' : 1000000,
                    '3' : 100000,           '7' : 5000000,
                    '4' : 200000,           '8' : 10000000,
                }
    if bahasa == 1:
        print('PILIH JUMLAH NOMINAL')
        print('1. 20.000            5. 500.000')
        print('2. 50.000            6. 1.000.000')
        print('3. 100.000           7. 5.000.000')
        print('4. 200.000           8. 10.000.000')
        print('BIAYA ADMIN RP 1.000')
        print('')

        # Inisialisasi data untuk struk
        nominal_isi_ulang = str(input('Pilih nominal isi ulang anda: '))
        admin_bank = 1000
        total_isi_ulang = daftar_pembelian[nominal_isi_ulang] + admin_bank
        os.system('cls' if os.name == 'nt' else 'clear')   
        
    elif bahasa == 2:
        print('SELECT AMOUNT ')
        print('1. 20.000            5. 500.000')
        print('2. 50.000            6. 1.000.000')
        print('3. 100.000           7. 5.000.000')
        print('4. 200.000           8. 10.000.000')
        print('ADMIN FEE RP 1.000')

        # Inisialisasi data untuk struk
        nominal_isi_ulang = str(input('Input Your Response Here: '))
        admin_bank = 1000
        total_isi_ulang = daftar_pembelian[nominal_isi_ulang] + admin_bank
        os.system('cls' if os.name == 'nt' else 'clear')   

    return nominal_isi_ulang, admin_bank, total_isi_ulang, daftar_pembelian 

def proses_bayar_2(bahasa, saldo, nama_lengkap, nomor_meter, id_pelanggan, daftar_pembelian, total_isi_ulang, nominal_isi_ulang, admin_bank):
    if bahasa == 1:
        print('HARAP MENUNGGU')
        print('TRANSAKSI ANDA SEDANG DIPROSES')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')  

        saldo -= total_isi_ulang
        waktu = datetime.now().isoformat(' ', 'seconds')
        print('TRANSAKSI TELAH BERHASIL')
        print('BERIKUT ADALAH STRUK ANDA')
        print('')
        time.sleep(1.5)
        os.system('cls' if os.name == 'nt' else 'clear') 

        # Mencetak struk pembayaran listrik
        print('---------------------BANK TPB SUKSES-----------------------')
        print('-------------TRUK PEMBELIAN LISTRIK PRABAYAR--------------')
        typing_effect(f'Nomor meter         : {nomor_meter}')
        typing_effect(f'IDPEL               : {id_pelanggan}')
        typing_effect(f'Nama Lengkap        : {nama_lengkap}')
        typing_effect(f'Jumlah              : {daftar_pembelian[nominal_isi_ulang]:,}'.replace(',', '.'))                    
        typing_effect(f'Total Bayar         : {total_isi_ulang:,}'.replace(',', '.'))
        typing_effect(f'Stroom/Token        : {random.randint(1000,9999)} {random.randint(1000,9999)} {random.randint(1000,9999)} {random.randint(1000,9999)}')
        typing_effect(f'Admin Bank          : {admin_bank:,}'.replace(',', '.'))
        typing_effect(f'Waktu Transaksi     : {waktu}')
        print('---------Jl. Let. Jend. Purn. Dr. (HC) Mashudi No.1-------')
        print('-----------------PLN MENYATAKAN STRUK INI-----------------')
        print('-------------SEBAGAI BUKTI PEMBAYARAN YANG SAH------------')
        print('')

    elif bahasa == 2:
        print('PLEASE WAIT')
        print('YOUR TRANSACTION IS BEING PROCESSED')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')  

        waktu = datetime.now().isoformat(' ', 'seconds')
        saldo -= total_isi_ulang
        print('TRANSACTION COMPLETED')
        print('HERE IS YOUR RECEIPT')
        print('')
        time.sleep(1.5)
        os.system('cls' if os.name == 'nt' else 'clear') 

        # Mencetak struk pembayaran listrik
        print('---------------------BANK TPB SUKSES----------------------')
        print('----------PREPAID ELECTRICITY PURCHASE RECEIPT------------')
        typing_effect(f'Meter Number        : {nomor_meter}')
        typing_effect(f'Customer ID         : {id_pelanggan}')
        typing_effect(f'Full Name           : {nama_lengkap}')
        typing_effect(f'Purchase Amount     : {daftar_pembelian[nominal_isi_ulang]:,}'.replace(',', '.'))                    
        typing_effect(f'TOTAL               : {total_isi_ulang:,}'.replace(',', '.'))
        typing_effect(f'Stroom/Token        : {random.randint(1000,9999)}, {random.randint(1000,9999)}, {random.randint(1000,9999)}, {random.randint(1000,9999)}')
        typing_effect(f'Admin Bank          : {admin_bank:,}'.replace(',', '.'))
        typing_effect(f'Transaction Time    : {waktu}')
        print('---------Jl. Let. Jend. Purn. Dr. (HC) Mashudi No.1-------')
        print('-----------------PLN DECLARES THIS RECEIPT----------------')
        print('----------------AS A VALID PROOF OF PURCHASE--------------')
        print('')
    
    return saldo

def bayar_3(bahasa, saldo, nama_lengkap, pilihan):
    # Menampilkan Kode Perusahaan
    kode_perusahaan = kode_bayar_3(bahasa)

    # Memasukkan data pelanggan        
    nomor_pelanggan, tagihan, biaya_admin, total_bayar = data_bayar_3(bahasa)

    # Konfirmasi data-data transaksi
    konfirmasi_pembayaran = konfirmasi_bayar_3(bahasa, kode_perusahaan, nomor_pelanggan, nama_lengkap, tagihan, biaya_admin, total_bayar)
    
    # Mencetak struk pembayaran PDAM  
    if(konfirmasi_pembayaran == 'y') and (saldo>=total_bayar): 
        pilihan, saldo = proses_bayar_3(bahasa, saldo, nama_lengkap, pilihan, konfirmasi_pembayaran, nomor_pelanggan, tagihan, biaya_admin, total_bayar)
    
    elif (konfirmasi_pembayaran == 'y') and (saldo<total_bayar) :
        print('MOHON MAAF SALDO ANDA TIDAK MENCUKUPI')
            
        pilihan = Menu_Kembali(bahasa, pilihan)
                
    else :
        print('MOHON TUNGGU SEBENTAR')
        print('ANDA AKAN DIALIHKAN KE MENU UTAMA')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear') 
        pilihan = 0

    return pilihan, saldo

def kode_bayar_3(bahasa):
    kode_perusahaan = {
                    "401" : 'PAM KOTA BOGOR'   , "406" : 'PAM KOTA CIREBON',
                    "402" : 'PAM KOTA CIANJUR' , "407" : 'PAM KOTA SUBANG' ,
                    "403" : 'PAM KOTA KUNINGAN', "408" : 'PAM KOTA CILEGON',
                    "404" : 'PAM KOTA SUMEDANG', "409" : 'PAM KOTA DEPOK'  ,
                    "405" : 'PAM KOTA SUKABUMI', "410" : 'PAM KOTA BANDUNG',
                }
    if bahasa == 1:
        typing_effect('MASUKKAN KODE PERUSAHAAN')
        typing_effect('DIIKUTI NOMOR PELANGGAN ANDA')
        typing_effect('CONTOH')
        typing_effect('Kode Perusahaan  : 401')
        typing_effect('No Pelanggan     : 1234567890')
        typing_effect('Tekan            : 4011234567890')
        print('')

        status_kode = str(input('Apakah anda ingin melihat daftar kode air minum/PDAM (y/n)? '))
        os.system('cls' if os.name == 'nt' else 'clear')   

        if (status_kode == 'y') :
            print('DAFTAR KODE PERUSAHAAN')
            print('PAM KOTA BOGOR               401')
            print('PAM KOTA CIANJUR             402')
            print('PAM KOTA KUNINGAN            403')
            print('PAM KOTA SUMEDANG            404')
            print('PAM KOTA SUKABUMI            405')
            print('PAM KOTA CIREBON             406')
            print('PAM KOTA SUBANG              407')
            print('PAM KOTA CILEGON             408')
            print('PAM KOTA DEPOK               409')
            print('PAM KOTA BANDUNG             410')
            time.sleep(7)
            os.system('cls' if os.name == 'nt' else 'clear') 
            
    elif bahasa == 2:
        typing_effect('ENTER COMPANY CODE')
        typing_effect('FOLLOWED BY YOUR CUSTOMER NUMBER')
        typing_effect('EXAMPLE')
        typing_effect('Company Code     : 1300')
        typing_effect('Customer Number  : 1234567890')
        typing_effect('Tekan            : 13001234567890')
        print('')
        
        status_kode = str(input('Do you wish to see the water/PDAM codes (y/n)? '))
        os.system('cls' if os.name == 'nt' else 'clear')

        if (status_kode == 'y') :
            print('COMPANY CODES LIST')
            print('PAM KOTA BOGOR               401')
            print('PAM KOTA CIANJUR             402')
            print('PAM KOTA KUNINGAN            403')
            print('PAM KOTA SUMEDANG            404')
            print('PAM KOTA SUKABUMI            405')
            print('PAM KOTA CIREBON             406')
            print('PAM KOTA SUBANG              407')
            print('PAM KOTA CILEGON             408')
            print('PAM KOTA DEPOK               409')
            print('PAM KOTA BANDUNG             410')
            time.sleep(7)
            os.system('cls' if os.name == 'nt' else 'clear') 
                
    return kode_perusahaan

def data_bayar_3(bahasa):
    if bahasa == 1:
        # Memasukkan data pelanggan
        print('MASUKKAN KODE PERUSAHAAN')
        print('DIIKUTI NOMOR PELANGGAN ANDA')
        print('CONTOH')
        print('Kode Perusahaan  : 401')
        print('No Pelanggan     : 1234567890')
        print('Tekan            : 4011234567890') 
        print('')

        # Inisialisasi dan perhitungan nilai untuk di struk
        nomor_pelanggan = str(input('Masukkan nomor pelanggan: '))
        os.system('cls' if os.name == 'nt' else 'clear')   
        tagihan       = random.randint(0,saldo-1000)
        biaya_admin   = 1000
        total_bayar   = tagihan + biaya_admin
            
        print('HARAP MENUNGGU')
        print('TRANSAKSI ANDA SEDANG DIPROSES')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')  
    

    elif bahasa == 2:
        print('ENTER COMPANY CODE')
        print('FOLLOWED BY YOUR CUSTOMER NUMBER')
        print('EXAMPLE')
        print('Company Code     : 1300')
        print('Customer Number  : 1234567890')
        print('Tekan            : 4011234567890')

        # Inisialisasi dan perhitungan nilai untuk di struk
        nomor_pelanggan = str(input('Input Your Response Here: '))
        os.system('cls' if os.name == 'nt' else 'clear')   
        tagihan       = random.randint(0,saldo-1000)
        biaya_admin   = 1000
        total_bayar   = tagihan + biaya_admin
            
        print('PLEASE WAIT')
        print('YOUR TRANSACTION IS BEING PROCESSED')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')   

    return nomor_pelanggan, tagihan, biaya_admin, total_bayar 

def konfirmasi_bayar_3(bahasa, kode_perusahaan, nomor_pelanggan, nama_lengkap, tagihan, biaya_admin, total_bayar):
    if bahasa == 1:
        print('---------------------------------------------------')
        print('KONFIRMASI PEMBAYARAN')
        print(f'TAGIHAN {kode_perusahaan[nomor_pelanggan[:3]]}')
        print(f'No Pelanggan     : {nomor_pelanggan[3:]}')
        print(f'Nama             : {nama_lengkap}')
        print(f'Tagihan          : {tagihan:,}'.replace(',', '.')) 
        print(f'Biaya admin      : {biaya_admin:,}'.replace(',', '.')) 
        print(f'Total Bayar      : {total_bayar:,}'.replace(',', '.')) 
        print('---------------------------------------------------')
        print('')

        konfirmasi_pembayaran = str(input('Ingin Melanjutkan Pembayaran (y/n)? '))
        os.system('cls' if os.name == 'nt' else 'clear')
        

    elif bahasa == 2:
        print('---------------------------------------------------')
        print('PAYMENT CONFIRMATION')
        print(f'INVOICE {kode_perusahaan[nomor_pelanggan[:3]]}')
        print(f'Customer Number  : {nomor_pelanggan[3:]}')
        print(f'Name             : {nama_lengkap}')
        print(f'Bill             : {tagihan:,}'.replace(',', '.')) 
        print(f'Admin fee        : {biaya_admin:,}'.replace(',', '.')) 
        print(f'TOTAL            : {total_bayar:,}'.replace(',', '.')) 
        print('---------------------------------------------------')
        print('')

        konfirmasi_pembayaran = str(input('Continue Payment (y/n)? '))
        os.system('cls' if os.name == 'nt' else 'clear')

    return konfirmasi_pembayaran

def proses_bayar_3(bahasa, saldo, nama_lengkap, pilihan, konfirmasi_pembayaran, nomor_pelanggan, tagihan, biaya_admin, total_bayar):
    if bahasa == 1:
        print('HARAP MENUNGGU')
        print('TRANSAKSI ANDA SEDANG DIPROSES')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        saldo -= total_bayar
        waktu = datetime.now().isoformat(' ', 'seconds')

        print('TRANSAKSI TELAH BERHASIL')
        print('Berikut adalah struk anda')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

        print('---------------------BANK TPB SUKSES----------------------')
        print('----------------STRUK PEMBAYARAN AIR/PDAM-----------------')
        typing_effect(f'No pelanggan        : {nomor_pelanggan}')
        typing_effect(f'Nama                : {nama_lengkap}')
        typing_effect(f'Tagihan             : {tagihan}')
        typing_effect(f'Biaya admin         : {biaya_admin:,}'.replace(',', '.')) 
        typing_effect(f'Total Bayar         : {total_bayar:,}'.replace(',', '.')) 
        typing_effect(f'Waktu Transaksi     : {waktu}') 
        print('---------Jl. Let. Jend. Purn. Dr. (HC) Mashudi No.1-------')
        print('-----------------PDAM MENYATAKAN STRUK INI----------------')
        print('-------------SEBAGAI BUKTI PEMBAYARAN YANG SAH------------')
        print('')
        pilihan = Menu_Kembali(bahasa, pilihan)
    
    elif bahasa == 2:
        print('PLEASE WAIT')
        print('YOUR TRANSACTION IS BEING PROCESSED')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        waktu = datetime.now().isoformat(' ', 'seconds')
        saldo -= total_bayar

        print('TRANSACTION COMPLETED')
        print('Here is your receipt')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

        print('---------------------BANK TPB SUKSES-----------------------')
        print('----------------WATER / PDAM BILL PAYMENT------------------')
        typing_effect(f'Customer Number     : {nomor_pelanggan}')
        typing_effect(f'Name                : {nama_lengkap}')
        typing_effect(f'Bill                : {tagihan}')
        typing_effect(f'Admin fee           : {biaya_admin:,}'.replace(',', '.')) 
        typing_effect(f'TOTAL               : {total_bayar:,}'.replace(',', '.')) 
        typing_effect(f'Transaction Time    : {waktu}') 
        print('-----------l. Let. Jend. Purn. Dr. (HC) Mashudi No.1-------')
        print('-----------------PDAM DECLARES THIS RECEIPT----------------')
        print('----------------AS A VALID PROOF OF PURCHASE---------------')
        print('')
        pilihan = Menu_Kembali(bahasa, pilihan)

    return pilihan, saldo

def ubah_pin(bahasa, pin, pilihan):
    if bahasa == 1:
        status_pin_masuk = False
        while status_pin_masuk == False :
            pin_masuk = str(input('Masukkan PIN anda: '))
            if (pin_masuk == pin) :
                status_pin_masuk = True
                status_pin = False 
                while (status_pin == False) :
                    pin = str(input('Masukkan PIN baru anda: '))
                    pin_konfirmasi = str(input('Konfirmasikan kembali PIN anda: '))
                    if (pin == pin_konfirmasi) :
                        os.system('cls' if os.name == 'nt' else 'clear')   
                        status_pin = True
                        print('PIN berhasil diubah!')
                        print('')
                            
                        # Ingin lanjut bertransaksi?
                        pilihan = Menu_Kembali(bahasa, pilihan)
                        return pin, pilihan
                    else :
                        print('PIN tidak sesuai!')
            else :
                print('PIN anda salah')
    
    elif bahasa == 2:
        status_pin_masuk = False
        while status_pin_masuk == False :
            pin_masuk = str(input('Enter your PIN: '))
            if (pin_masuk == pin) :
                status_pin_masuk = True
                status_pin = False 
                while (status_pin == False) :
                    pin = str(input('Enter your new PIN: '))
                    pin_konfirmasi = str(input('Please confirm your new PIN: '))
                    if (pin == pin_konfirmasi) :
                        os.system('cls' if os.name == 'nt' else 'clear')   
                        status_pin = True
                        print('PIN changed successfully!')
                        print('')
                            
                        # Ingin lanjut bertransaksi?  
                        pilihan = Menu_Kembali(bahasa, pilihan)  
                        return pin, pilihan                 
                    else :
                        print('Wrong PIN entered!')
            else :
                print('Wrong PIN entered')
                    
def setor_tunai(bahasa,saldo,pilihan):
    if bahasa == 1:
        print('SETORAN TUNAI BANK TPB SUKSES')
        print('')
        print('SILAKAN MASUKKAN UANG YANG AKAN DISETOR')
        print('NOMINAL YANG DITERIMA')
        print('    - 50.000         ')
        print('    -100.000         ')
        print('')
        print('MOHON PERHATIAN UNTUK:')
        print('- MEMASTIKAN DENOMINASI UANG')
        print('- MERAPIKAN UANG ANDA')
        print('')
        lembar_50k = int(input('Masukkan jumlah lembaran Rp 50.000 yang akan disetor: '))
        lembar_100k = int(input('Masukkan jumlah lembaran Rp 100.000 yang akan disetor: '))
        os.system('cls' if os.name == 'nt' else 'clear')
        print('HARAP MENUNGGU')
        print('TRANSAKSI ANDA SEDANG DIPROSES')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('SETORAN TUNAI BANK TPB SUKSES')
        print('')
        if lembar_50k == 0 and lembar_100k == 0:
            print('Anda akan dikembalikan ke menu utama')
            time.sleep(2)
            return 0, saldo
        if lembar_50k > 0:
            print(f' 50000 X {lembar_50k}   = {50000 * lembar_50k}')
        if lembar_100k > 0:
            print(f'100000 X {lembar_100k}   = {100000 * lembar_100k}')
        setoran = 50000 * lembar_50k + 100000 * lembar_100k
        print(f'TOTAL        = {setoran}')
        print('')
        print('Konfirmasi Setor')
        print('1. Setor')
        print('2. Batal')
        konfirmasi_setoran = int(input())
        os.system('cls' if os.name == 'nt' else 'clear')
        
        if konfirmasi_setoran == 1:
            print('HARAP MENUNGGU')
            print('TRANSAKSI ANDA SEDANG DIPROSES')
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            waktu = datetime.now().isoformat(' ', 'seconds')
            saldo += setoran
            print('---------------------------------------------------')
            print('SETORAN TUNAI BANK TPB SUKSES')
            print(f'Nama                 : {nama_lengkap}')
            print(f'TOTAL                : {setoran:,}'.replace(',', '.')) 
            print(f'Saldo Rekening Baru  : {saldo:,}'.replace(',', '.')) 
            print(f'Waktu Transaksi      : {waktu}') 
            print('---------------------------------------------------')
            print('')
            pilihan = Menu_Kembali(bahasa, pilihan)
                        
        else:
            print('Transaksi Dibatalkan')
            print('Silakan Ambil Kembali Uang Tunai Anda')
            print('')
            time.sleep(2)
            pilihan = Menu_Kembali(bahasa, pilihan)
        
    elif bahasa == 2:
        print('BANK TPB SUKSES CASH DEPOSIT')
        print('')
        print('PLEASE INSERT THE CASH TO BE DEPOSITED')
        print('ACCEPTED CASH DENOMINATIONS')
        print('    - 50.000         ')
        print('    -100.000         ')
        print('')
        print('PLEASE ENSURE TO:')
        print('- CONFIRM THE CASH DENOMINATIONS')
        print('- ARRANGE YOUR CASH PROPERLY')
        print('')
        lembar_50k = int(input('Enter the number of Rp 50.000 bills to be deposited: '))
        lembar_100k = int(input('Enter the number of Rp 100.000 bills to be deposited: '))
        os.system('cls' if os.name == 'nt' else 'clear')
        print('PLEASE WAIT')
        print('YOUR TRANSACTION IS BEING PROCESSED')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('BANK TPB SUKSES CASH DEPOSIT')
        print('')
        if lembar_50k == 0 and lembar_100k == 0:
            print('You will be returned to the main menu')
            time.sleep(2)
            return 0, saldo
        if lembar_50k > 0:
            print(f' 50000 X {lembar_50k}   = {50000 * lembar_50k}')
        if lembar_100k > 0:
            print(f'100000 X {lembar_100k}   = {100000 * lembar_100k}')
        setoran = 50000 * lembar_50k + 100000 * lembar_100k
        print(f'TOTAL        = {setoran}')
        print('')
        print('Deposit Confirmation')
        print('1. Deposit')
        print('2. Cancel')
        konfirmasi_setoran = int(input())
        os.system('cls' if os.name == 'nt' else 'clear')
        
        if konfirmasi_setoran == 1:
            print('PLEASE WAIT')
            print('YOUR TRANSACTION IS BEING PROCESSED')
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            waktu = datetime.now().isoformat(' ', 'seconds')
            saldo += setoran
            print('---------------------------------------------------')
            print('BANK TPB SUKSES CASH DEPOSIT')
            print(f'Name                 : {nama_lengkap}')
            print(f'TOTAL                : {setoran:,}'.replace(',', '.')) 
            print(f'New Account Balance  : {saldo:,}'.replace(',', '.')) 
            print(f'Transaction Time     : {waktu}') 
            print('---------------------------------------------------')
            print('')
            pilihan = Menu_Kembali(bahasa, pilihan)
            
        else:
            print('Transaction Cancelled')
            print('Please Take Back Your Cash')
            print('')
            time.sleep(2)
            pilihan = Menu_Kembali(bahasa, pilihan)

    return pilihan, saldo
                    
#Fungsi Typing Effect di Terminal
def typing_effect(text, delay=0.025):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line after typing is done

def kartu_keluar():
    print('Silakan Ambil Kartu Anda')
    print('')
    time.sleep(0.3)
    card = [
                "|=============|",
                "|             |",
                "|             |",
                "|    KARTU    |",
                "|     ATM     |",
                "|             |",
                "|             |",
                "|=============|"
            ]
    
    # Cetak kartu 
    for i in range(len(card)):
        os.system('cls' if os.name == 'nt' else 'clear')
        # Cetak bagian bawah kartu bertahap hingga ke atas
        for line in card[-(i+1):]:
            print(line)
        time.sleep(0.2)

    print('')
    print('Terima Kasih telah menggunakan ATM BANK TPB SUKSES')
    time.sleep(3)
    return

#ALGORITMA UTAMA
#Pembuatan Akun yang memberikan output pin, saldo
pin, saldo, nama_lengkap, tanggal_lahir = pembuatan_akun()

# TAHAP ATM
# Memasukkan Kartu
bahasa = kartu_masuk()

# ATM
if (bahasa == 1) or (bahasa == 2) :
    # Memasukkan dan Mengecek PIN yang dimasukkan
    pin = pin_masuk(bahasa, pin)

    # Menampilkan menu yang bisa dipilih

    os.system('cls' if os.name == 'nt' else 'clear')     
    pilihan = Menu(bahasa)
    os.system('cls' if os.name == 'nt' else 'clear')     

    # Masuk ke menu-menu yang disediakan 
    while ((pilihan == 0) or (pilihan == 1) or (pilihan == 2) or (pilihan == 3) or (pilihan == 4) or (pilihan == 5) or (pilihan == 6)):
        if (pilihan == 0) :
            os.system('cls' if os.name == 'nt' else 'clear')   
            pilihan = Menu(bahasa)
            os.system('cls' if os.name == 'nt' else 'clear')  
        
        # Menu informasi saldo       
        elif (pilihan == 1) :
            pilihan = cek_Saldo(bahasa, saldo, pilihan)   

        # Menu penarikan tunai 
        elif (pilihan == 2) :
            pilihan, saldo = penarikan_tunai(bahasa, saldo, pilihan)
            
        # Menu transfer
        elif (pilihan == 3) :
            pilihan, saldo = transfer_bank(bahasa, saldo, pilihan)
        
        # Menu pembayaran (Telepon, PLN, dan PDAM)
        elif (pilihan == 4) :
            pilihan, saldo = pembayaran(bahasa, saldo, nama_lengkap, pilihan)

        # Mengubah PIN
        elif (pilihan == 5) :
            pin, pilihan = ubah_pin(bahasa, pin, pilihan)
            
        # Setor tunai
        elif (pilihan == 6):
            pilihan, saldo = setor_tunai(bahasa,saldo,pilihan)
            
    # Keluar dari ATM
    kartu_keluar()

