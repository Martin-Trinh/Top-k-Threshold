class Video:
    def __init__(self, title, channel_title, views, likes, dislikes, comment_cnt, aggr_val) -> None:
        self.title = title
        self.channel_title = channel_title
        self.views = views
        self.likes = likes
        self.dislikes = dislikes
        self.comment_cnt = comment_cnt
        self.aggr_val = aggr_val

    def __lt__(self, vid):
        return self.aggr_val < vid.aggr_val