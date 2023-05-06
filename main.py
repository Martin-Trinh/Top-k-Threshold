from flask import Flask, render_template, request, session, flash
import pandas as pd
from classes.VideoAttr import VideoAttr
from classes.ParseReq import ParseReq
from algorithm import *

app = Flask(__name__)
app.secret_key = "secret"

#Loading data from csv to dataframe
df = pd.read_csv('./data/processes_data.csv')

@app.route("/")
def home():
    data = []
    access_cnt = 0
    param = ParseReq(request)
    if len(param.vid_attr) == 0:
        param.vid_attr.append("views")
    if param.rows_amount != 0:
        if(param.algorithm == "threshold"):
            attr = VideoAttr(df,param)
            print("Threshold")
            data , access_cnt = threshold_top_k(df, attr, param)
        else:
            print("Naive")
            data, access_cnt = naive_top_k(df, param)


    return render_template("home.html", columns=df.columns, data=data , access_cnt=access_cnt, rows_amount= len(data) )

if __name__ == "__main__":
    app.run(debug=True)