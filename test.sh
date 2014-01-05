if [ "$(pidof python /root/forpy/port-forward.py)" ]
then
  echo "True"
else
  echo "False"
fi
