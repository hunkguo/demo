import datetime
def formatGMTime(timestamp):
    GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
    a = datetime.datetime.strptime(timestamp, GMT_FORMAT) + datetime.timedelta(hours=8)
    return a



def convertISODate(timestamp):    
    GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
    a = datetime.datetime.strptime(timestamp, GMT_FORMAT).isoformat()
    return a


