#!/bin/sh

curl --verbose --user $NOIP_USERPASSWORD --user-agent "$NOIP_USERAGENT" \
 https://dynupdate.no-ip.com/nic/update?hostname=$NOIP_HOSTNAME&myip=$NOIP_IP

 sleep 5s