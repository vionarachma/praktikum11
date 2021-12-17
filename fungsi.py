def tampilkan(nama):
    print("hello", nama, ". selamat datang")


tampilkan("ari")
nama = "ari santoso"
tampilkan(nama)

# fungsi dengan return value


def hitung(a, b):
    return a + b


print(hitung(4, 5))
a = 10
b = 15
print(hitung(a, b))

# fungsi arbitrary arguments


def tampil(*names):
    for nama in names:
        print("hello", nama, ". apa kabar ?")


print(tampil("ari"))
print(tampil("ari", "dina", "ratna"))
