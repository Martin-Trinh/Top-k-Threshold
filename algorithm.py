from classes.Video import Video
from classes.ParseReq import ParseReq
from classes.VideoAttr import VideoAttr
import heapq

def calc_aggr_val():
    pass

def calc_threshold(aggr_func, data):
    pass
def get_aggr_func(name):
    pass

def aggr_max():
    pass

def aggr_sum():
    pass

def naive_top_k():
    pass

def threshold_top_k(videos, vid_attr : VideoAttr, param : ParseReq):
    aggr_func = get_aggr_func(param.aggr_func)
    access_cnt = 0
    read_video = set()
    heap = []
    heapq.heapify(heap)
    for i in range(0, vid_attr.len()):
        threshold_data = []
        access_cnt += 1
        for attr in vid_attr.columns:
            if attr in param.vid_attr:
                row , val = vid_attr.attr_db[attr][i]
            threshold_data.append(val)
        # calculate threshold
        threshold_val = calc_threshold(aggr_func, threshold_data)
        # locate video in database
        vid = videos.iloc[row]
        # calc aggregated value for video's attribute
        aggr_data = []
        for attr in vid_attr.columns:
            if attr in param.vid_attr:
                aggr_data.append(vid[attr])
        aggr_val = calc_aggr_val(aggr_func, aggr_data)
        # store videos in heap
        if(len(heap) < param.rows_amount):
            heapq.heappush(heap,(aggr_val, vid))
        else:
            if heap[0][0] < aggr_val:
                heapq.heapreplace(heap,(aggr_val, vid))
        if aggr_val >= threshold_val and len(heap) == param.rows_amount:
            break
    res = [val[1] for val in heap]
        
        