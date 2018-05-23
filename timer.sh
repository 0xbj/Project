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

Timecount(){
# Set variables to your desired time.

hour=0
min=0
sec=0

    if [[ $2 == "hour" ]] #|| [[ $2 == "-h" ]]
        then
            hour=$1
    elif [[ $2 == "minute" ]] #|| [[ $2 == "-m" ]]
        then
            min=$1
    elif [[ $2 == "second" ]] #|| [[ $2 == "-s" ]]
        then
            sec=$1
    fi


       # begin hour while loop - while hour 
       #variable is greater than or equal to 0 do minute loop
       while [[ $hour -ge 0 ]]; do
                # begin minute loop - while min variable 
                #is greater than or equal to 0 do second loop
                while [[ $min -ge 0 ]]; do
                        # begin second loop - while sec variable is greater
                        # than or equal to 0 print time left
                        while [[ $sec -ge 0 ]]; do
                                # echo time on same line so it overwrites last                                             # line, makes it look like countdown
                                echo -ne $BYellow"     $hour:$min:$sec\033[0K\r" ;tput sgr0
                                # Decrease the sec variable by 1 
                                #each iteration of loop to countdown
                                let "sec=sec-1"
                                # wait a second before removing a second
                                # from the countdown clock
                                sleep 1
                        # End second loop
                        done
                        # Set second timer back to 59 to start new minute
                        sec=59
                        # Decrease min variable by 1 to remove a
                        # minute off the countdown
                        let "min=min-1"
                # end minute loop
                done
                # Set minute timer back to 59 to start new hour
                min=59
                # decrease the hour by 1 to remove hour off the countdown
                let "hour=hour-1"
        # end hour loop
        done 
        echo " "
}

out() {
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


if [ "$EUID" -ne 0 ] || [ "$2" == "" ] || [ "$2" != "hour" ] && [ "$2" != "minute" ] && [ "$2" != "second" ] || ! [[ "$1" =~ ^[0-9]+$ ]] 
  then
    echo " " 
    echo -e $BRed"    ERROR | Run as Root / Argument Not Match" ;tput sgr0
    echo " "
    echo -e $BWhite"    [+] Example"
    echo "          >   sudo ./timer 1 hour"
    echo "          >   sudo ./timer 5 minute"
    echo "          >   sudo ./timer 15 second" ; tput sgr0

    exit
fi

    
echo " "
echo -en $BWhite" Input Your Command >> "; read Command ; echo " "; tput sgr0; echo -e " "

#errorCommand="$($Command --help  2>/dev/null | wc -l)"
errorCommand=`$Command --help  2>/dev/null | wc -l`
#echo $errorCommand

if [ "$errorCommand" -lt 5 ]
    then 
        echo -e $BRed"    ERROR | Command Input Not Found, Exiting" ;tput sgr0
        echo " "
        exit
    else
            Timecount $1 $2
fi


echo -e " \n"
echo -e $BCyan"  [+]  Time UP, Running Input Command ...." ;tput sgr0
echo " "

state=$(echo "$Command" | wc -m) #; echo $state ; sleep 999999

if [[ $state -lt 2 ]]
    then
        echo -e $BRed"  [-]  No Input Command , Exiting" ;tput sgr0
        out
fi

#echo -e $BCyan"  [Command]  "$Command ;tput sgr0

if $Command ; then
    echo " "
    echo -e $BGreen"  [+]  Command [$Command] succeeded"
    out
else
    echo " "
    echo -e $BRed"  [-]  Command [$Command] failed"
    out
fi
