from flask import Flask

app=Flask(__name__)


@app.route('/')
def index():
    return "installation Successul"

if __name__ =="__main__":
    app.run()