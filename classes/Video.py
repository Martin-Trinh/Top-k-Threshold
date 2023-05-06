class Video :
    def __init__(self,video, aggr_val) -> None:
        self.title = video.title
        self.channel_title = video.channel_title
        self.views = video.views
        self.likes = video.likes
        self.dislikes = video.dislikes
        self.comment_count = video.comment_count
        self.aggr_val = aggr_val
    
    def __lt__(self, rhs):
        return self.aggr_val < rhs.aggr_val