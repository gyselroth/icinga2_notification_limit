import datetime

class LimitChecker(object):
    @staticmethod
    def Check(counter, maximum, updated, timerange):
        if (updated + datetime.timedelta(0, timerange)) < datetime.datetime.utcnow():
            return 1
        elif counter < maximum:
            return counter + 1
        else:
            return None
