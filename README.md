# README
This program provides the ability to limit the notifications sent by icinga2 per recipient.
A limit is defined as the maxmimum number of notifications in a specified time interval (e.g. 100 notifications per hour).

## INSTALLATION (example)
### Requirements
* pybuilder
### Program
```
pyb
cd target/dist/icinga2_notification_limit-<VERSION>/
python setup.py
```
### Database
```
CREATE TABLE icinga_notification_limits (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    maximum INT UNSIGNED NOT NULL,
    timerange INT UNSIGNED NOT NULL,
    PRIMARY KEY (id)
);


CREATE TABLE icinga_notification_counters (
    id INT UNSIGNED AUTO_INCREMENT,
    recipient VARCHAR(50) NOT NULL,
    limitId INT UNSIGNED NOT NULL,
    counter INT UNSIGNED DEFAULT 0,
    updated TIMESTAMP DEFAULT '0000-00-00 00:00:00',
    PRIMARY KEY (id),
    FOREIGN KEY (limitId) REFERENCES icinga_mailnotification_limits(id)
);
```
## CONFIGURATION (example)
### Database
* The `maxmimum` field of the `*_limits` table represents the maximum number of notifications for the limit.
* The `timerange` field of the `*_limits` table represents the time interval in seconds for the limit.
* The `recipient` field of the `*_counters` table represents an identifier of the targeted recipient (e.g. email address for mail notification).
* The `limitId` field of the `*_counters` table links the recipient to a limit.
_by now, only one limit per recipient is supported!_

```
INSERT INTO icinga_notification_limits (maximum, timerange) VALUES (100, 60);

INSERT INTO icinga_notification_counters (recipient, limitId) VALUES ('jucker@gyselroth.com', 1);
```

## USAGE
The program itself does __not__ invoke any invocation.
Instead, the program returns a value of 0, if the notification should be send and a value of 1 if the notification should not be send.
Therefore the program can be used in any script.
Tip: Look at the shellscript examples for usage with the default mail-notification-scripts in examples folder.
