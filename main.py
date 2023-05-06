from flask import Flask, render_template, request, session, flash
import pandas as pd
from classes.VideoAttr import VideoAttr
from classes.ParseReq import ParseReq
from classes.Video import Video
from algorithm import *
import time
app = Flask(__name__)
app.secret_key = "secret"

#Loading data from csv to dataframe
df = pd.read_csv('./data/processes_data.csv')

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
            attr = VideoAttr(df,param)
            print("Threshold")
            start = time.time()
            data , access_cnt = threshold_top_k(df, attr, param)
            end = time.time()
            time_measured = end - start
        else:
            print("Naive")
            start = time.time()
            data, access_cnt = naive_top_k(df, param)
            end = time.time()
            time_measured = end - start

    
    return render_template("home.html", columns=df.columns, data=data , access_cnt=access_cnt, rows_amount= len(data), time = round(time_measured, 6) )

if __name__ == "__main__":
    app.run(debug=True)