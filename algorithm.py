from classes.ParseReq import ParseReq
from classes.VideoAttr import VideoAttr
import heapq


def calc_aggr_val(name, data):
    if name == "max":
        return max(data)
    elif name == 'mean':
        return sum(data) / len(data)
    else:
        return min(data)
    
def naive_top_k(data, param: ParseReq):
    access_cnt = 0
    heap = []
    heapq.heapify(heap)
    for index, vid in data.iterrows():
        access_cnt += 1
        aggr_val = data.loc[index, param.vid_attr].agg(param.aggr_func)
        vid['aggr_val'] = aggr_val
        if(len(heap) < param.rows_amount):
            heapq.heappush(heap,(aggr_val, vid))
        else:
            heapq.heappushpop(heap,(aggr_val, vid))
    res = [val[1] for val in heapq.nlargest(param.rows_amount,heap)]
    return res, access_cnt

def threshold_top_k(data, vid_attr : VideoAttr, param : ParseReq):
    access_cnt = 0
    heap = []
    heapq.heapify(heap)
    processed = set()
    for i in range(0, vid_attr.len()):
        threshold_data = []
        access_cnt += 1
        for attr in param.vid_attr:
            index , val = vid_attr.attr_db[attr][i]
            
            threshold_data.append(val)
            # locate video in database
            vid = data.iloc[index].copy()
            # calc aggregated value for video's attribute
            aggr_val = vid.loc[param.vid_attr].agg(param.aggr_func)
            vid['aggr_val'] = aggr_val
            # add video to the heap
            if index not in processed:
                processed.add(index)
                if(len(heap) < param.rows_amount):
                    heapq.heappush(heap,(aggr_val, vid))
                else:
                    heapq.heappushpop(heap,(aggr_val, vid))

        # calculate threshold
        threshold_val = calc_aggr_val(param.aggr_func, threshold_data)
        # break if aggregate value is 
        if len(heap) == param.rows_amount and heapq.nsmallest(1,heap)[0][0] <= threshold_val:
            break

    res = [val[1] for val in heapq.nlargest(param.rows_amount,heap)]
    return res, access_cnt
