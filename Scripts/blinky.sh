#!/bin/bash
gpio mode 0 out
gpio mode 1 out
COUNT=1

while((COUNT<11))
do
	gpio write 1 1
	gpio write 0 1
	sleep 1
	((COUNT ++))
	gpio write 1 0
	gpio write 0 0
	sleep 1
done
