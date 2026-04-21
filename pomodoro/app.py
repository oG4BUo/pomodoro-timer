from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import date

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/save", methods=["POST"])
def save():
    minutes = request.json["minutes"]
    today = str(date.today())
    
    # 既存の記録を読み込む
    if os.path.exists("record.json"):
        with open("record.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {}
    
    # 今日の記録に追加する
    if today in data:
        data[today] += minutes
    else:
        data[today] = minutes
    
    # 保存する
    with open("record.json", "w", encoding="utf-8") as f:
        json.dump(data, f)
    
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)