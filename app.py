from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
        <body style="background-color: black; color: #00FF00; font-family: 'Courier New', Courier, monospace; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0;">
            <div>
                <h1>> Hello, World_</h1>
                <h2>> Questo è il mio progetto DevOps.</h2>
            </div>
        </body>
    '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
