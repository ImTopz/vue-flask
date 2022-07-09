from flask import Flask

app = Flask(__name__)


@app.route('/api')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/data')
def data_detect():

if __name__ == '__main__':
    app.run()
