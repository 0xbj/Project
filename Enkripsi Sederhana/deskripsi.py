import os 
import time

os.system('cls')

keyOpen = open("key.txt",'r')
splitKey = keyOpen.read().split()

# print(splitKey)																	# DEBUG

_input = input("\n\t[?] Masukkan Chiper Text : ")

index = []
hasil = []

for x in range(len(_input)):
	for y in range(len(splitKey)):
		if(_input[x] == splitKey[y]):
			index.append(y)
		else:
			pass

print("\n\n[+] Index Plain Text : {}".format(index[:]))									# DEBUG

for i in range(len(index)):
	# if(index[i] - 2 < 0 ):
	# 	c = 64
	# 	index[i] = c - index[i]
	if(index[i] == 0):																	# di sini key = -2, jadi kalau hasil setelah di kurang 2 jadi -, maka di lakukan pengecekan ini
		index[i] = 63																	# akal-akalan kalau index nya bernilai 0, maka akan jadi 63, tidak -2
	elif(index[i] == 1):
		index[i] = 64																	# kalau index bernilai 1, maka jika di kuran -2 akan jadi 64 bukan -1
	else:
		index[i] = index[i] - 2															# kalau nilai lebih dari 0 dan 1, maka di kurang seperti biasa

print("\n\n[+] Index Chiper Text : {}".format(index[:]))								# DEBUG

for i in range(len(index)):
	bufferIndex = index[i]
	bufferHasil = splitKey[bufferIndex]

	hasil.append(bufferHasil)

print("\n\n[+] Hasil Chiper : {}\n\n".format(hasil))

for i in range(len(hasil)):
	print(hasil[i],end='')
print("\n")

keyOpen.close()