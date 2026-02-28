from kalkulator import pengurangan, pembagian, penjumlahan, perkalian

x = int(input("Masukkan angka: "))
y = int(input("Masukkan angka: "))
op = input("Masukkan operator (+,-,/,*): ")

if op == "+":
    print(penjumlahan(x, y))
elif op == "-":
    print(pengurangan(x, y))
elif op == "/":
    print(pembagian(x,y))
elif op == "*":
    print(perkalian(x,y))
else: 
    print("Operator unknown")