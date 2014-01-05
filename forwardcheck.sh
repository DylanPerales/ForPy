#!/bin/bash
PATH=/usr/bin:/bin

if [ "$(pidof python /root/forpy/port-forward.py)" ]
then
 print "No Issues"
else
  python /root/forpy/port-forward.py &
  sleep 5
  if [ "$(pidof python /root/forpy/port-forward.py)" ]
  then
    echo "ERROR: Process not running, Started Process Successfully!" |  mutt -s "ERROR: [TITAN] Port-Forward" dperales@gmail.com
  else
    echo "ERROR: Process not running, FAILED TO START PROCESS!" |  mutt -s "ERROR: [TITAN] Port-Forward" dperales@gmail.com
  fi
fi
