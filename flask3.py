from flask import Flask

app=Flask(__name__)

@app.route('/home')
def home():
    return 'Welcome to Home Screen'

@app.route('/vinay')
def vinay():
    return 'Welcome to Vinay World!'

if __name__='__main__':
    app.run(debug=True)
