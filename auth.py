from data import data_akun
from utils import input_teks, clear_terminal, enter

def register():
    clear_terminal()
    try:
        print("========= REGISTER =========")
        username_baru = input_teks("Masukkan username baru: ").lower()
        password_baru = input_teks("Masukkan password baru: ").lower()
        print("============================")

        if username_baru in data_akun:
            raise ValueError("\nUsername sudah terpakai!")

    except ValueError as e:
        print(f"{e}")
        return

    else:  
        data_akun[username_baru] = [password_baru]
        print("\nRegistrasi berhasil! Silakan login.")

    finally:
        enter("Tekan enter untuk kembali ke menu awal...")


def login():
    clear_terminal()
    try:
        print("========= LOGIN =========")
        username = input_teks("Masukkan username: ").lower()
        password = input_teks("Masukkan password: ").lower()
        print("=========================")

        if data_akun[username] != password:
            raise ValueError("Password salah! Silakan login ulang.")

    except KeyError:
        print("\nAkun tidak terdaftar! Silakan melakukan registrasi.")
        return

    except ValueError as e:
        print(f"{e}")
        return

    else:
        print(f"Login berhasil! Selamat datang, {username}.")
        enter("Tekan Enter untuk melanjutkan...")