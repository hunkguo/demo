########################################################################
from datetime import datetime
class BaseData(object):
    def __init__(self):
        """Constructor"""
        pass

 
class NewsData(BaseData):
    def __init__(self):
        """Constructor"""
        super(NewsData, self).__init__()
        self.title = ''       
        self.published = datetime.now()
        self.content = ''    
        self.tags = {}   