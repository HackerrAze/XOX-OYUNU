import os,time
from random import randint
os.system('clear')

print("="*71)
print("\t\t\t    XOX OYUNU!")
print("YARADILDI: 20.01.2022")
print("SON GÜNCELLENME: 20.01.2022")
print("="*71)

a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
k = 8
z = 9
while True:
	print("",a,"|",b,"|",c,)
	print("","-----------")
	print("",d,"|",e,"|",f)
	print("","-----------")
	print("",g,"|",k,"|",z)
	
	sec = str(input("Seçenek Giriniz: "))
	
	if sec == "1":
		if a == "O":
			continue
		a = "X"
	elif sec == "2":
		if b == "O":
			continue
		b = "X"
	elif sec == "3":
		if c == "O":
			continue
		c = "X"
	elif sec == "4":
		if d == "O":
			continue
		d = "X"
	elif sec == "5":
		if e == "O":
			continue
		e = "X"
	elif sec == "6":
		if f == "O":
			continue
		f = "X"
	elif sec == "7":
		if g == "O":
			continue
		g = "X"
	elif sec == "8":
		if k == "O":
			continue
		k = "X"
	elif sec == "9":
		if z == "O":
			continue
		z = "X"
	else:
		print("Yalnış Seçim!")
		time.sleep(2)
		os.system('clear')
		continue
		
		
	if a == b == c or c == e == g or a == e == z or d == e == f or g == k == z or a == d == g or b == e == k or c == f == z:
		print("="*71)
		print("Kazandınız!")
		print("="*71)
		break
	while True:
		ras = randint(1,9)
		if ras == 1:
			if a == "X":
				continue
			if a == "O":
				continue
			a = "O"
			break
		elif ras == 2:
			if b == "X":
				continue
			if b == "O":
				continue
			b = "O"
			break
		elif ras == 3:
			if c == "X":
				continue
			if c == "O":
				continue
			c = "O"
			break
		elif ras == 4:
			if d == "X":
				continue
			if d == "O":
				continue
			d = "O"
			break
		elif ras == 5:
			if e == "X":
				continue
			if e == "O":
				continue
			e = "O"
			break
		elif ras == 6:
			if f == "X":
				continue
			if f == "O":
				continue
			f = "O"
			break
		elif g == 7:
			if a == "X":
				continue
			if g == "O":
				continue
			g = "O"
			break
		elif ras == 8:
			if k == "X":
				continue
			if k == "O":
				continue
			k = "O"
			break
		elif ras == 9:
			if z == "X":
				continue
			if z == "O":
				continue
			z = "O"
			break
		else:
			print("Hata Oluştu!")
			break
	if a == b == c or c == e == g or a == e == z or d == e == f or g == k == z or a == d == g or b == e == k or c == f == z:
		print("="*71)
		print("Rakib Kazandı!")
		print("="*71)
		break
		
		
		
		