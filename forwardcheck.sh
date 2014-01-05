#!/bin/bash
PATH=/usr/bin:/bin

if [ "$(pidof python /root/forpy/port-forward.py)" ]
then
  # NO ISSUES
  true
else
  # Try to restart script
  python /root/forpy/port-forward.py &
  sleep 5
  if [ "$(pidof python /root/forpy/port-forward.py)" ]
  then
    # Script was started successfully
    echo "ERROR: Process not running, Started Process Successfully!" |  mutt -s "ERROR: [TITAN] Port-Forward" email@domain.com # Edit with real Address
  else
    # Script did not start successfully
    echo "ERROR: Process not running, FAILED TO START PROCESS!" |  mutt -s "ERROR: [TITAN] Port-Forward" email@domain.com # Edit with real Address
  fi
fi
