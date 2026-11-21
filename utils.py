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