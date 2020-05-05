from flask import Flask,add_url_rule

app=Flask(__name__)

def index():
    return 'Welcome to my second program with different decorator approach'

@app.add_url_rule('/','index'index)
