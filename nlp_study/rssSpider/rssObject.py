########################################################################
class BaseData(object):
    def __init__(self):
        """Constructor"""
        self.gatewayName = ''         # Gateway名称        
        self.rawData = None                     # 原始数据

 
class RssData(BaseData):
    def __init__(self):
        """Constructor"""
        super(RssData, self).__init__()
                
        self.title = ''           
        self.summary = ''    
        self.link =''       