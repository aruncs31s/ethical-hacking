#!/bin/bash

HEIGHT=15
WIDTH=40
CHOICE_HEIGHT=4
TITLE="Bash menu"
MENU="options:"

OPTIONS=(1 "tig"
 	 7 "ranger")

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
		tig
                ;;
        2)
                lazygit
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

