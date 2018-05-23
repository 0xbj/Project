import os
import random
import time
import platform

if (platform.system() == 'Linux'):
	os.system('clear')
elif (platform.system() == 'Windows'):
	os.system('cls')
else:
	print('ERROR , Cannot Clear Terminal')

var1 = " Moderator Subuh\t: "
var2 = " Moderator Taraweh\t: "
var3 = " Moderator Bilal\t: "
var4 = " Moderator Buka Puasa\t: "

var5 = " Bersih Masjid\t: "
var6 = " Bersih Pak Sigit\t: "

kel1 = ['Fitri Amalia','Darsono','Nurfitriani','Bagus']
kel2 = ['Rubianti','Mei','Dimas','Hadijah','Adian','']
kel3 = ['Hidayat','Nias','Mariam','Eka','Ricky','']
kel4 = ['Ita Parwita','Qadiran','Miftahul Jannah','Sofyan','Ines','' ]
kel5 = ['Rosdiana','Zukhruf','Bulkis','Lina']
kel6 = ['Evi Amalia','Ahmad','Estik Komaidah','Dhewa']
kel7 = ['Rabiatul','Indras','Henny','Vijay','Zahra','']

hasilPath_ = r"JADWAL KARTINI 2018 FIX !!!!!!!.txt"
hasilWrite = open(hasilPath_,'w')

listPathCowok = open('source_cowok.txt')
listReadCowok = listPathCowok.read().splitlines()

listPathCewek = open('source_cewek.txt')
listReadCewek = listPathCewek.read().splitlines()

temp = []
tempCewek = []

color = ['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m','\033[1;37m']
index_color = 4


tanggal = 23
counter_pengajarTPA = 1
bulan = " Mei 2018"

while True:

	moderatorBukaPuasa = ['iqbal','ammar','aziz','rofi']

	myList1 = random.sample(range(0,len(listReadCowok)),3)

	myList2 = random.sample(range(0,len(listReadCowok)),6)

	myList3 = random.sample(range(0,len(listReadCewek)),6)

	# myList3 = random.sample(range(0,len(listReadCowok)),15)

	if(tanggal == 31):
		tanggal = 1
		bulan = "Juni 2018"
	if(index_color == 6):
		index_color = 4

	if(counter_pengajarTPA % 2 == 0):
		list_pengajar_kel1 = kel1[0:2] #
		list_pengajar_kel2 = kel2[0:3]
		list_pengajar_kel3 = kel3[0:3]
		list_pengajar_kel4 = kel4[0:3]
		list_pengajar_kel5 = kel5[0:2] #
		list_pengajar_kel6 = kel6[0:2] #
		list_pengajar_kel7 = kel7[0:3]

		item = 'bagus','adian','eka','sofyan','vijay','ricky'

		for i in range(0,5):
			moderatorBukaPuasa.append(item[i])
	else:
		list_pengajar_kel1 = kel1[2:4]
		list_pengajar_kel2 = kel2[3:6]
		list_pengajar_kel3 = kel3[3:6]
		list_pengajar_kel4 = kel4[3:6]
		list_pengajar_kel5 = kel5[2:4]
		list_pengajar_kel6 = kel6[2:4]
		list_pengajar_kel7 = kel7[3:6]

		item = 'darsono','dimas','qadiran','zukhruf','ahmad'

		for i in range(0,4):
			moderatorBukaPuasa.append(item[i])
	
	time.sleep(1)

	for i in myList1:
		temp.append(listReadCowok[i])

	for i in myList2:
		temp.append(listReadCowok[i])

	for i in myList3:
		tempCewek.append(listReadCewek[i])


	hasilWrite.write("\t%d %s \n1 %s %s \n2 %s %s \n3 %s %s \n4 %s %s\n\n"%(tanggal,bulan,var1,temp[0],var2,temp[1],var3,temp[2],var4,random.choice(moderatorBukaPuasa)))

	hasilWrite.write("5 %s %s - %s - %s - %s - %s - %s \n6 %s %s - %s - %s -  %s - %s - %s \n\n"%(var5,temp[3],temp[4],temp[5],tempCewek[0],tempCewek[1],tempCewek[2],var6,temp[6],temp[7],temp[8],tempCewek[3],tempCewek[4],tempCewek[5]))

	hasilWrite.write("List Pengajar TPA :")
	hasilWrite.write("\nkel 1 : %s - %s" %(list_pengajar_kel1[0],list_pengajar_kel1[1]) )
	hasilWrite.write("\nkel 2 : %s - %s - %s" %(list_pengajar_kel2[0],list_pengajar_kel2[1],list_pengajar_kel2[2]))
	hasilWrite.write("\nkel 3 : %s - %s - %s" %(list_pengajar_kel3[0],list_pengajar_kel3[1],list_pengajar_kel3[2]))
	hasilWrite.write("\nkel 4 : %s - %s - %s" %(list_pengajar_kel4[0],list_pengajar_kel4[1],list_pengajar_kel4[2]))
	hasilWrite.write("\nkel 5 : %s - %s" %(list_pengajar_kel5[0],list_pengajar_kel5[1]))
	hasilWrite.write("\nkel 6 : %s - %s" %(list_pengajar_kel6[0],list_pengajar_kel6[1]))
	hasilWrite.write("\nkel 7 : %s - %s - %s" %(list_pengajar_kel7[0],list_pengajar_kel7[1],list_pengajar_kel7[2]))
	hasilWrite.write("\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n")



	print("\t%d %s \n1 %s %s \n2 %s %s \n3 %s %s \n4 %s %s\n"%(tanggal,bulan,var1,temp[0],var2,temp[1],var3,temp[2],var4,random.choice(moderatorBukaPuasa)))

	print("5 %s %s - %s - %s - %s - %s - %s \n6 %s %s - %s - %s -  %s - %s - %s \n\n"%(var5,temp[3],temp[4],temp[5],tempCewek[0],tempCewek[1],tempCewek[2],var6,temp[6],temp[7],temp[8],tempCewek[3],tempCewek[4],tempCewek[5]))

	print("List Pengajar TPA :")
	print("kel 1 : %s - %s" %(list_pengajar_kel1[0],list_pengajar_kel1[1]) )
	print("kel 2 : %s - %s - %s" %(list_pengajar_kel2[0],list_pengajar_kel2[1],list_pengajar_kel2[2]))
	print("kel 3 : %s - %s - %s" %(list_pengajar_kel3[0],list_pengajar_kel3[1],list_pengajar_kel3[2]))
	print("kel 4 : %s - %s - %s" %(list_pengajar_kel4[0],list_pengajar_kel4[1],list_pengajar_kel4[2]))
	print("kel 5 : %s - %s" %(list_pengajar_kel5[0],list_pengajar_kel5[1]))
	print("kel 6 : %s - %s" %(list_pengajar_kel6[0],list_pengajar_kel6[1]))
	print("kel 7 : %s - %s - %s" %(list_pengajar_kel7[0],list_pengajar_kel7[1],list_pengajar_kel7[2]))
	print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

	tanggal += 1
	index_color += 1
	counter_pengajarTPA += 1

	temp.clear()
	tempCewek.clear()

listPathCowok.close()
hasilWrite.close()
