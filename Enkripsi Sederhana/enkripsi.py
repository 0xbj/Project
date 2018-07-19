import os 
import time

os.system('cls')

keyOpen = open("key.txt",'r')														# buka file key.txt , disini ada list key yang dijadikan inti dari enkripsi
splitKey = keyOpen.read().split()													# menjadikan array semua nilai yang ada di file key.txt, di simpan ke variabel splitKey

# print(splitKey)																	# DEBUG

_input = input("\n\t[?] Masukkan Plain Text : ")

index = []																			# untuk menampung index yang cocok dari user input sama key dari file key.txt
hasil = []																			# menampung hasil jika sudah di tambah +2

for x in range(len(_input)):														# nested loop untuk mencari nilai variabel _input yang cocok dengan variable splitKey
	for y in range(len(splitKey)):
		if(_input[x] == splitKey[y]):
			index.append(y)															# jika cocok, maka masukkan ke variable array index
		else:
			pass

print("\n\n[+] Index Plain Text : {}".format(index[:]))									# DEBUG

for i in range(len(index)):															# looping untuk menambahkan isi dari variabel index ke index + 2, ini kuncinya. tidak boleh lebih dari 64
	index[i] = (index[i] + 2) % 65

print("\n\n[+] Index Chiper Text : {}".format(index[:]))								# DEBUG

for i in range(len(index)):															# looping untuk menyamakan index dari variabel index[] ke string yang ada di variabel splitKey
	bufferIndex = index[i]
	bufferHasil = splitKey[bufferIndex]

	hasil.append(bufferHasil)														# hasil di simpan di variabel array hasil

print("\n\n[+] Hasil Chiper : {}\n\n".format(hasil))

for i in range(len(hasil)):															# print hasil dalam string, bukan tampilan array
	print(hasil[i],end='')
print("\n")

keyOpen.close()																		# close file key.txt yang di buka di awal