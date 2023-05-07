from classes.ParseReq import ParseReq
from classes.VideoAttr import VideoAttr
from classes.Video import Video
import heapq


def calc_aggr_val(name, data):
    if name == "max":
        return max(data)
    elif name == 'mean':
        return sum(data) / len(data)
    else:
        return min(data)
    
def naive_top_k(data, param):
    access_cnt = 0
    heap = []
    heapq.heapify(heap)
    for index, vid in data.iterrows():
        access_cnt += 1
        # calculate aggr_val for each row
        aggr_val = round(data.loc[index, param.vid_attr].agg(param.aggr_func), 2)
        # heap.append(Video(vid,aggr_val))
        if(len(heap) < param.rows_amount):
            heapq.heappush(heap,(aggr_val,  Video(vid,aggr_val)))
        else:
            heapq.heappushpop(heap,(aggr_val,  Video(vid,aggr_val)))
        # heap.sort(reverse=True)
    res = [val[1] for val in heapq.nlargest(param.rows_amount,heap)]
    return  res, access_cnt

def threshold_top_k(data,vid_attr :VideoAttr, param):
    access_cnt = 0
    heap = []
    heapq.heapify(heap)
    for i in range(0, vid_attr.len()):
        threshold_data = []
        access_cnt += 1
        index = 0
        for attr in param.vid_attr:
            # get index and value in database from sorted list
            index , val = vid_attr.attr_db[attr][i]
            threshold_data.append(val)
        # locate video in database
        vid = data.iloc[index]
        # calc aggregated value for video's attribute
        aggr_val = round(vid.loc[param.vid_attr].agg(param.aggr_func), 2)
        # add video to the heap
        vid_tuple = (aggr_val, Video(vid,aggr_val))
        if vid_tuple not in heap:
            if(len(heap) < param.rows_amount):
                heapq.heappush(heap, vid_tuple)
            else:
                heapq.heappushpop(heap,vid_tuple)

        # calculate threshold
        threshold_val = calc_aggr_val(param.aggr_func, threshold_data)
        # break if aggregate value is 
        if len(heap) == param.rows_amount and heap[0][0] <= threshold_val:
            break

    res = [val[1] for val in heapq.nlargest(param.rows_amount,heap)]
    return res, access_cnt
