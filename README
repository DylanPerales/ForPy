# ForPy

Used to Forward a port and log its connection.
Very simple, used to verify a connection was made or as a proxy

### port-forward.py

Modify Lines 9 and 10 with your listening Address and Port.
Modify Lines 11 and 12 with your target Address and Port.

A log will be generated in the log/ folder with the following format:

```
port-forward_20140105.log
```

### forwardcheck.sh

This can be used in a crontab entry to verify the process is running.
Example:

```
15 * * * * sh /path/to/forwardcheck.sh
```

Line 7 occurs when the script is running
Line 15 occurs when the script is not running but is restarted successfully
Line 18 occurs when the script is not running and not restarted successfully
Please modify accordingly. In my example I am using Mutt with msmtp.