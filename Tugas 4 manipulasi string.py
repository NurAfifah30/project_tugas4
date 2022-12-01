a = "Universitas Ubharajaya"
print("jumlah = ",len(a))

txt = "Universitas Ubharajaya cari karakter"
print("cari" in txt)

txt = "Universitas Ubharajaya cari karakter"
if "Ubharajaya1" in txt:
  print("data di temukan.")
else:
  print("data tidak di temukan.")


b = "Universitas Ubharajaya memotong  karakter dari posis yang ditentukan"
print(b[2:5])

b = "Universitas Ubharajaya"
print(b[:5])

b = "Universitas Ubharajaya"
print(b[2:])

b = "Universitas Ubharajaya memotong  karakter dari posis yang ditentukan"
print(b[6:11])

b = "Universitas Ubharajaya"
print(b[-5:])
print(b[:-2])
print(b[-5:-2])


b = "  universitas ubharajaya huruf besar semua  "
print(b.upper())
print(b.lower())
print(b.strip()) ##menhilangkan karakter kosong

a="mengganti karakter"
print(a.replace("i", "y"))

##memecah kalimat berdasarkan karakter 
a = "Ubhara,jaya"
b = a.split(",")
print(b)
a = "Ubhara/jaya"
b = a.split("/")
print(b)
##menggabungkan karakter
a = "Jamilah"
b = "Hasan"
c = a + " " + b
print(c)

quantity = 3
itemno = 567
price = 49.95
myorder = "format {} number {} dan {} string."
print(myorder.format(quantity, itemno, price))