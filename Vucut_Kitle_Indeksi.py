#Vücut Kitle İndeksi

kilo=int(input("Kilonuzu giriniz(kg):"))
boy=float(input("Boyunuzu giriniz(m):"))
vki=kilo/(boy*boy)

if(vki<=18.5):
    print("Zayıf")
elif(18.5<=vki<=24.9):
    print("Normal")
elif(25<=vki<=29.9):
    print("Fazla Kilolu")
elif(30<=vki<=34.9):
    print("1.Dereceden Obez")
elif(35<=vki<=39.9):
    print("2.Dereceden Obez")
else:
    print("3.Dereceden Obez")