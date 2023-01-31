#!/bin/bash

HEIGHT=15
WIDTH=40
CHOICE_HEIGHT=4
TITLE="Bash menu"
MENU="options:"

OPTIONS=(1 "Payload generator"
 	 2 "main page")

CHOICE=$(dialog --clear \
                --backtitle "Bash launcher by @aruncs31s" \
                --title "$TITLE" \
                --menu "$MENU" \
                $HEIGHT $WIDTH $CHOICE_HEIGHT \
                "${OPTIONS[@]}" \
                2>&1 >/dev/tty)

clear
case $CHOICE in
	
	1)
		bash ./Scripts/payload-generator-script1.sh
                ;;
        2)
		firefox --new-window https://github.com/Ethical-h4ckers
                ;;
        3)
                peaclock --config "peaclock/cfg/binary"
                ;;
        4)
                mpd;ncmpcpp
                ;;
        5)
                links
                ;;
        6)
                fsmon
                ;;
        7)
                cd /sdcard ; ranger
                ;;
esac

