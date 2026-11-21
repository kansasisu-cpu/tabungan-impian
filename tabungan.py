from utils import clear_terminal, input_teks, enter, input_angka

def buat_tabungan(username):
    clear_terminal()
    try:
        print("========= BUAT TABUNGAN =========")
        nama_tabungan = input_teks("Nama tabungan: ").lower()
        target = input_angka("Target: Rp", min=20000)
        print("============================")
        