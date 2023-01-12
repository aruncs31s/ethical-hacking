#!/bin/sh:/bin/bash

if 
gcc  CVE-2022-0847-exploit.c -o exploit1
gcc CVE-2022-0847-exploit.c  -o exploit2
