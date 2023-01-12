#!/bin/bash

if [[(-f /bin/gcc)]];then 
gcc  CVE-2022-0847-exploit.c -o exploit1
gcc CVE-2022-0847-exploit.c  -o exploit2
elif [[ (-f /bin/clang) ]]
then
gcc  CVE-2022-0847-exploit.c -o exploit1
gcc CVE-2022-0847-exploit.c  -o exploit2
elif 
echo " no compiler found"
fi
