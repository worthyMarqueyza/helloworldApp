from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
        <body style="background-color: black; color: #00FF00; font-family: 'Droid Sans Mono', monospace; font-size: 16px; margin: 20px;">
            Hello, friend_
        </body>
    '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
