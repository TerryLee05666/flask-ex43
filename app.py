from flask import Flask, render_template

app = Flask(__name__)

# 這個路徑對應 Exercise 43 截圖上的要求
@app.route('/')
def index():
    return 'Index Page'

# 這個路徑順便示範如何載入 templates 資料夾裡面的網頁
@app.route('/home')
def home():
    return render_template('home.html')