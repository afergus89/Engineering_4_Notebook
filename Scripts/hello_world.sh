#!/bin/bash
str="Hello World!"
COUNT=1
while ((COUNT < 11))
do 
	echo $str
	((COUNT++))
done
