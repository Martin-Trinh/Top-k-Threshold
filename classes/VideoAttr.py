class VideoAttr:
    def __init__ (self, dataFrame):
        self.columns = dataFrame.columns
        self.attr_db = {
            'views' : list(dataFrame['views'].sort_values(ascending=False).items()),
            'likes' : list(dataFrame['likes'].sort_values(ascending=False).items()),
            'comment_count' : list(dataFrame['comment_count'].sort_values(ascending=False).items())
        }
    def len(self):
        return len(self.views_col)
