from classes.ParseReq import ParseReq
class VideoAttr:
    def __init__ (self, dataFrame, param: ParseReq):
        self.length = dataFrame.shape[0]
        self.attr_db = {}
        for attr in param.vid_attr:
            self.attr_db[attr] = list(dataFrame[attr].sort_values(ascending=False).items())
    def len(self):
        return self.length
