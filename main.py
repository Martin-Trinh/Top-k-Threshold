from flask import Flask, render_template, request
import pandas as pd
from classes.VideoAttr import VideoAttr
from classes.ParseReq import ParseReq
from algorithm import *

app = Flask(__name__)

#Loading data from csv to dataframe
df = pd.read_csv('./data/processes_data.csv')
# Sort each column
attr = VideoAttr(df)
columns = df.columns[2:5]
checked_col = []

@app.route("/", methods=["GET", "POST"])
def home():
    param = ParseReq(request)
    if(param.algorithm == "threshold"):
        threshold_top_k()
    else:
        naive_top_k()
    # print(request.args)
    return render_template("home.html", columns = columns, checked_col = checked_col)

if __name__ == "__main__":
    app.run(debug=True)