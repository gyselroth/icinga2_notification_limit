# README
## INSTALLATION
```
CREATE TABLE icinga_mailnotification_limits (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    maximum INT UNSIGNED NOT NULL,
    timerange INT UNSIGNED NOT NULL,
    PRIMARY KEY (id)
);


CREATE TABLE icinga_mailnotification_counters (
    id INT UNSIGNED AUTO_INCREMENT,
    recipient VARCHAR(50) NOT NULL,
    limitId INT UNSIGNED NOT NULL,
    counter INT UNSIGNED DEFAULT 0,
    updated TIMESTAMP DEFAULT '0000-00-00 00:00:00',
    PRIMARY KEY (id),
    FOREIGN KEY (limitId) REFERENCES icinga_mailnotification_limits(id)
);
```
## CONFIGURATION
```
INSERT INTO icinga_mailnotification_limits (maximum, timerange) VALUES (100, 60);

INSERT INTO icinga_mailnotification_counters (recipient, limitId) VALUES ('jucker@gyselroth.com', 1);
```
