import os
from time import sleep


print("")
print("Ujian Dasar")
print("")

nama = input("Nama anda : ")
kelas = input("Kelas : ")
absen = input("absen : ")
sleep(1)

os.system('clear')


print ("     QUIZ     ")
print("*jangan menekan enter")
print("1)")
print("2)")
print("3)")
print("4)")
sleep(5)
os.system('clear')


def soal_pertama():
    print("")
    print("1) apa yang di maksud dengan python")
    print("a.python adalah")
    print("b.python adalah")
    soal_pertama=input("Jawaban yang benar adalah : ")
    print("")
    if soal_pertama == 'a' :
        sleep (1)
        print ("jawaban yang benar adalah b")
        point_pertama = 0

    if soal_pertama == 'b' :
        print("jawaban anda benar")
        print("anda memperoleh 10 point")
        point_pertama = 10
    return point_pertama

point_pertama = soal_pertama()


def soal_kedua():
    print("")
    print("2) apa yang di maksud dengan seni ?")
    print("a. seni adalah blabla")
    print("b. seni adalah blablasaa")
    soal_kedua=input("jawaban yang paling tepat adalah :")
    print("")
    if soal_kedua == 'a' :
        print("jawaban anda benar")
        print("anda memperoleh 10 poin")
        point_kedua = 10
    if soal_kedua == 'b' :
        print("jawaban yang benar adalah a")
        point_kedua = 0
    return point_kedua

point_kedua = soal_kedua()

def soal_ketiga():
    print("")
    print("2) apa yang di maksud dengan seni ?")
    print("a. seni adalah blabla")
    print("b. seni adalah blablasaa")
    soal_ketiga=input("jawaban yang paling tepat adalah :")
    print("")
    if soal_ketiga == 'a' :
        print("jawaban anda benar")
        print("anda memperoleh 10 poin")
        point_ketiga = 10
    if soal_ketiga == 'b' :
        print("jawaban yang benar adalah a")
        point_ketiga = 0
    return point_ketiga

point_ketiga = soal_ketiga()

sleep (5)
os.system('clear')
print("")
print("======================")
print("Nama        : ",nama)
print("Kelas       : ",kelas)
print("Absen       : ",absen)
point= point_pertama + point_kedua + point_ketiga
print("Total Point : ",point)

nilai = 100 / 30
score = nilai * point
print("Nilai kamu  : ",score)

if score > 75 :
    print ("Selamat",nama,"kamu lulus")
if score < 75 : 
    print (nama,"kamu tidak lulus")
    print(":(")


print("")
print("")
print("")
print("")
print("")
print("@melsen888")