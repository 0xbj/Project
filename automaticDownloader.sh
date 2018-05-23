#!/bin/bash

BBlack='\033[1;30m'       # Black
BRed='\033[1;31m'         # Red
BGreen='\033[1;32m'       # Green
BYellow='\033[1;33m'      # Yellow
Yellow='\033[0;33m'
BBlue='\033[1;34m'        # Blue
BPurple='\033[1;35m'      # Purple
BCyan='\033[1;36m'        # Cyan
BWhite='\033[1;37m'       # White
On_Green='\033[42m'

#trap '' INT TSTP

_main_quite(){

STATUS=$(/usr/bin/pgrep wget | wc -l)

count=$_input_count

digits=${#count}

	#	awal perulangan
	while [ $STATUS -eq 0 ]; do

		#	status informasi [urutan] [url]
		echo -e $BGreen"[+] Downloaded file - $_input_count "$BYellow"<== ($_input_url)" ;tput sgr0
		echo " "

		#	masukin command ke variable agar bisa di detect jika gagal
		#Command=`wget $_input_url/$count.mp3` # INI MASIH ERROR

		#	DUA VERSI PERULANGAN DENGAN MENGGUNAKAN ARGUMEN PADA COMMAND

			#	perulangan if untuk cek status wget gagal atau tidsak
			if wget $_input_url$_input_count$_input_format #2> /dev/null
				then
					echo -e $BGreen"[+] SUCCES"
				else
					echo -e $BRed"[-] ERROR | Exiting"
					exit
			fi				

		#	finising
		echo -n " "
		echo  " "
		sleep 1

		#	increment
		count=$(printf "%0${digits}d\n" "$((10#$count + 1))")

	#	membuat batas akhir, ga guna kalo uda ada if status
	#if [ $count == '060' ] ; then exit ; fi
	done

#	dialog keluar
echo " [+] Download File Complete , Exiting"
sleep 2
exit
}



#_main_verbose(){exit}


clear

echo -en $BWhite" [?] Input URL >> " ; read _input_url
#_input_url='https://download.quranicaudio.com/quran/sa3ood_al-shuraym'
_input_count=1
echo -en $BWhite" [?] Input Number list >> " ;read _input_count

echo -en $BWhite" [?] Input Format File >> " ;read _input_format; tput sgr0
 
if [ "$1" = "-v" ] ; then
	_main_verbose
elif [ "$1" = "-q" ]; then
	_main_quite
else
			echo " "
			echo " ERROR | Argument Not Found"
			echo "[Options]"
			echo " -v => verbose || -q => quiets"

fi



