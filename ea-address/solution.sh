#/bin/bash
grep -o -rnw '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' The-Works-of-Edgar-Allen-Poe-Vol-2.txt
#line 6735: 127.0.0.1
# remove the ip address and use this command:
m5dsum The-Works-of-Edgar-Allen-Poe-Vol-2.txt
#ef192f313be2a2e21e6bdf03e98f8a02  The-Works-of-Edgar-Allen-Poe-Vol-2.txt
#The hash  output is the flag:ef192f313be2a2e21e6bdf03e98f8a02
