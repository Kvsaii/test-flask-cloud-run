from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Dockerised Flask"

@app.route("/route")
def hello():
    return "This is not the 32A"



if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')
