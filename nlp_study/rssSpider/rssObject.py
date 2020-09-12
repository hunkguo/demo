########################################################################
from datetime import datetime
import bson.objectid
class BaseData(object):
    def __init__(self):
        """Constructor"""
        pass

 
class RssData(BaseData):
    def __init__(self):
        """Constructor"""
        super(RssData, self).__init__()
        self.ObjectId = bson.ObjectId() 
        self.title = ''       
        self.published = datetime.now()
        self.summary = ''    
        self.link =''    
        self.tags = {}   