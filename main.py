from auth import register, login

print("1. Register")
print("2. Login")
pilihan = input("Masukkan pilihan:")

if pilihan == "1":
    register()

elif pilihan == "2":
    login()