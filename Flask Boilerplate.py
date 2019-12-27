from flask import Flask
app = Flask(__name__)

@app.route('/')
def default_page():
    return 'Greetings humans!'

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host="localhost")
