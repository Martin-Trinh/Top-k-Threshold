from flask import request

class ParseReq:
    def __init__ (self, req):
        self.algorithm = req.args.get('algo_select')
        self.aggr_func = req.args.get('aggr_func')
        k = req.args.get('rows-amount')
        if k is None or k == '':
            self.rows_amount = 0
        else:
            self.rows_amount = int(k)
        self.vid_attr = []
        for attr in req.args.getlist('vid_attr'):
            self.vid_attr.append(attr)