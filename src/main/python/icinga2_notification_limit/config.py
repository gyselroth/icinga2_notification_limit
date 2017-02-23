"""Reader for mysql configuration"""
import os
import re


class ConfigReaderError(Exception):
    """Error in ConfigReader"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class ConfigReader(object):
    DEFAULT_CONFIG_FILE = '/etc/icinga2/features-enabled/ido-mysql.conf'
    REGEX = {
        'host': re.compile('^\s*host\s*=\s*("|\')(.*)("|\')'), \
        'user': re.compile('^\s*user\s*=\s*("|\')(.*)("|\')'), \
        'password': re.compile('^\s*password\s*=\s*("|\')(.*)("|\')'), \
        'database': re.compile('^\s*database\s*=\s*("|\')(.*)("|\')'), \
        'table_prefix': re.compile('^\s*table_prefix\s*=\s*("|\')(.*)("|\')')
    }

    def __init__(self, configFile=None):
        if configFile is None:
            configFile = ConfigReader.DEFAULT_CONFIG_FILE

        self.config = {'host': None, 'user': None, 'password': None, \
        'database': None, 'table_prefix': None}

        try:
            with open(configFile, 'r') as config:
                for line in config:
                    # TODO: reduce unnecessary iterations (e.g. all config settings already known)
                    self.__matchLine(line)
        except IOError as exception:
            raise ConfigReaderError(str(exception))

    def __matchLine(self, line):
        for key in ConfigReader.REGEX:
            if self.config[key] is None:
                regex = ConfigReader.REGEX[key]
                match = regex.search(line)
                if match:
                    self.config[key] = match.group(2)

    def getConfig(self):
        return self.config
