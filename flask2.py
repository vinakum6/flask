from flask import Flask

app=Flask(__name__)

def index():
    return 'Welcome to my second program with different decorator approach'

app.add_url_rule('/','index',index)

if __name__=='__main__':
    app.run(debug=True)
