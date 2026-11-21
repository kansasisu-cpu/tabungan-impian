import os

def clear_terminal():
    os.system("cls")

def input_teks(pesan):
    teks = input(pesan).strip()

    if teks == "":
        raise ValueError("Input tidak boleh kosong!")
    return teks

def enter(pesan="Tekan Enter untuk kembali..."):
    input("\n" + pesan)

def input_angka(pesan, min = 0, boleh_kosong = False):
    teks = input(pesan).strip()

    if teks == "":
        if boleh_kosong:
            return None
        raise ValueError("Input tidak boleh kosong!")
    
    if not teks.isdigit():
        raise ValueError("Input harus berupa angka bulat positif!")
    
    nilai = int(teks)

    if nilai < min:
        raise ValueError(f"Nilai minimal yang diperbolehkan adalah {min}!")
    
    return nilai