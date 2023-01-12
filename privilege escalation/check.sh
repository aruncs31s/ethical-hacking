#!/bin/bash
check=$(uname -r | cut -b 1-5)
 if [ $check -ls 5.4.0 ] ; then 
 echo affected 
 fi