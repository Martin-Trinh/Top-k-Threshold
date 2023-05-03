from flask import request

class ParseReq:
    def __init__ (self, req):
        self.algorithm = req.args.get('algo_select')
        self.aggr_func = req.args.get('aggr_func')
        self.rows_amount = int(req.args.get('rows-amount'))
        self.vid_attr = []
        for attr in req.args.getlist('vid_attr'):
            self.vid_attr.append(attr)