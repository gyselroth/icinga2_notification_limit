#!/bin/sh
icinga-notification-limit -r $USEREMAIL
if [ $? -ne 1 ]
then
  /etc/icinga2/scripts/mail-host-notification.sh
fi
