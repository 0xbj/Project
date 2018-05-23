#!/bin/bash
echo " "
#echo -n " Number Of Looping >> "
#read Looping

echo -n " Delay Time >> "
read delay



urutan=1
while true
#while [ $urutan -lt $Looping ] || true
do

	echo -e "\e[3$(( $RANDOM * 5 / 32767 + 1 ))m"
	echo " "
	echo "++++++++++++++++++++++++++++++++++++++++++"
	echo "					$urutan					"
	echo "++++++++++++++++++++++++++++++++++++++++++"
	echo " " ; tput sgr0
	
	cat /proc/cpuinfo | grep "cpu MHz"

	echo " "

	sensors | grep °C ; tput sgr0

	echo " "

	free -h 

	urutan=$(( $urutan + 1 ))
	sleep $delay
done
