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
normal=$(tput sgr0)

trap '' INT TSTP

if [ "$EUID" -ne 0 ] || [ "$1" == "" ] || [ "$1" != "-h" ] && [ "$1" != "-m" ] && [ "$1" != "-s" ] || ! [[ "$2" =~ ^[0-9]+$ ]] 
  then
    echo " " 
    echo -e $BRed"    ERROR | Run as Root / Argument Not Match" ;tput sgr0
    echo " "
    echo -e $BWhite"    [+] Example"
    echo "          >   sudo ./timer -h 1"
    echo "          >   sudo ./timer -m 5"
    echo "          >   sudo ./timer -s 15" ; tput sgr0

    exit
fi

#f [ "$#" -lt "2" ] ; then 
#	echo "Incorrect usage ! Example:" 
#	echo './countdown.sh -d  "Jun 10 2011 16:06"' 
#	echo 'or' 
#	echo './countdown.sh -m  90' 
#	exit 1 
#fi 

_timeCount_(){

now=`date +%s` 
 
#if [ "$1" = "-d" ] ; then 
#	until=`date -d "$2" +%s` 
#	sec_rem=`expr $until - $now` 
#	echo "-d" 
#	if [ $sec_rem -lt 1 ]; then 
#		echo "$2 is already history !" 
#	fi 
#fi 
 
if [ "$1" = "-m" ] ; then 
	until=`expr 60 \* $2` 
	until=`expr $until + $now` 
	sec_rem=`expr $until - $now` 
	echo "-m" 
	if [ $sec_rem -lt 1 ]; then 
		echo "$2 is already history !" 
	fi 
fi 
##########################################
if [ "$1" = "-h" ] ; then 
	until=`expr 3600 \* $2` 
	until=`expr $until + $now` 
	sec_rem=`expr $until - $now` 
	echo "-m" 
	if [ $sec_rem -lt 1 ]; then 
		echo "$2 is already history !" 
	fi 
fi 

if [ "$1" = "-s" ] ; then 
	until=$2 
	until=`expr $until + $now` 
	sec_rem=`expr $until - $now` 
	echo "-m" 
	if [ $sec_rem -lt 1 ]; then 
		echo "$2 is already history !" 
	fi 
fi 
###########################################
_R=0
_C=7
tmp=0
percent=0
total_time=0
col=`tput cols`
col=$[ $col -5 ]
_date=`date`

while [ $sec_rem -gt 0 ]; do 
	clear 
	echo -e $BYellow"$_date"
	let sec_rem=$sec_rem-1 
	interval=$sec_rem 
	seconds=`expr $interval % 60` 
	interval=`expr $interval - $seconds` 
	minutes=`expr $interval % 3600 / 60` 
	interval=`expr $interval - $minutes` 
	hours=`expr $interval % 86400 / 3600` 
	interval=`expr $interval - $hours` 
	days=`expr $interval % 604800 / 86400` 
	interval=`expr $interval - $hours` 
	weeks=`expr $interval / 604800` 
	echo "----------------------------" 
	echo " "
	#echo "Seconds: " $seconds 
	#echo "Minutes: " $minutes 
	#echo "Hours:   " $hours 
	#echo "Days:    " $days 
	#echo "Weeks:   " $weeks 
	echo -e "\t\t\t\t  $hours:$minutes:$seconds"
	echo -ne "["

	progress=$[$progress + 1]
	if [ $total_time -lt 1 ] ; then
		total_time=$[$hours * 3600 + $minutes * 60 + $seconds]
	fi
	
	printf -v f "%$(echo $_R)s>" ; printf "%s\n" "${f// /#}"
	_C=7
	tput cup 4 $col
	tput civis
	tmp=$percent
	percent=$[$progress * 100 / $total_time]
	printf "]%d%%" $percent
	tmp=$[$percent - $tmp]

	_R=$[ $col * $percent / 100 ]

	sleep 1
done
#printf "\n"
tput cnorm
tput sgr0
}


_out_() {
    tput sgr0
        echo " "
        echo " "

            for (( i = 0; i < 52; i++ )); do
                echo -n "+"
            done
    
        echo " "
        echo -e $BBlue "Thank You & Have a Good Day || FAKHRIZAL ASSHIDDIQ"; tput sgr0
    
            for (( i = 0; i < 52; i++ )); do
                echo -n "+"
            done
    
        echo " "
    exit
}

echo " "
echo -en $BWhite" Input Your Command >> "; read Command ; echo " "; tput sgr0; echo -e " "

# JANGAN DI HAPUS !!!
#_array=( $Command )
#echo ${_array[0]}
#echo ${_array[1]}

#_help1=`${_array[0]} --help 2> /dev/null`

if hash $Command 2>/dev/null
    then 
    echo " Succes"
    _timeCount_ $1 $2
    else
        echo -e $BRed"    ERROR | Command Input Not Found, Exiting" ;tput sgr0
        echo " "
        exit
fi


echo -e " \n"
echo -e $BCyan"  [+]  Time UP, Running Input Command ...." ;tput sgr0
echo " "

state=$(echo "$Command" | wc -m) #; echo $state ; sleep 999999

if [[ $state -lt 2 ]]
    then
        echo -e $BRed"  [-]  No Input Command , Exiting" ;tput sgr0
        _out_
fi

#echo -e $BCyan"  [Command]  "$Command ;tput sgr0

if $Command ; then
    echo " "
    echo -e $BGreen"  [+]  Command [$Command] succeeded"
    _out_
else
    echo " "
    echo -e $BRed"  [-]  Command [$Command] failed"
    _out_
fi