from flask import Flask, request
app = Flask(__name__, static_folder='static')

pid = 0

@app.route('/')
def root():
    return 'hello world'

@app.route('/static/<path:path>')
def send_js(path):
        return send_from_directory('static', path)

@app.route('/set')
def set_pic():
    global pid
    pid = int(request.args.get('id'))
    return '1'

@app.route('/get')
def get_pic():
    return str(pid)

if __name__ == '__main__':
    app.run()

