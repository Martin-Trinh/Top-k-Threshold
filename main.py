from flask import Flask, render_template, request
import pandas as pd
from classes.VideoAttr import VideoAttr
from classes.ParseReq import ParseReq
from algorithm import *
import time

app = Flask(__name__)

#Loading data from csv to dataframe
df = pd.read_csv('./data/US_vid_processed.csv')
vid_attr = VideoAttr(df)

@app.route("/")
def home():
    data = []
    access_cnt = 0
    time_measured = 0
    param = ParseReq(request)
    if len(param.vid_attr) == 0:
        param.vid_attr.append("views")
    if param.rows_amount != 0:
        if(param.algorithm == "threshold"):
            start = time.time()
            data , access_cnt = threshold_top_k(df,vid_attr,param)
            time_measured = time.time() - start
        else:
            start = time.time()
            data, access_cnt = naive_top_k(df, param)
            time_measured = time.time() - start

    
    return render_template("home.html", columns=df.columns, data=data , access_cnt=access_cnt, rows_amount= len(data), time = round(time_measured, 6) , dataset_len = df.shape[0])

if __name__ == "__main__":
    app.run(debug=True)