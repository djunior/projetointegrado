#!/bin/bash
logFile=`date "+%Y-%m-%d"`.txt
logDir="/var/local/log/gosurf"
export logger="$logDir/$logFile"

log(){
	echo "[`basename $0` - `date +%c`]  $*" >> $logger
}

clean_log(){
	rm -f $logger
}
