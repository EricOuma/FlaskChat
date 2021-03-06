from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = '84go47049v784g0478'
socketio = SocketIO(app)

@app.route('/', methods=['GET', 'POST'])
def sessions():
    return render_template('session.html')

def message_received(methods=['GET', 'POST']):
    print('message was received')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=message_received)

@socketio.on('myevent')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: '+ str(json))
    socketio.emit('my response', json, callback=message_received)

if __name__ == "__main__":
    socketio.run(app)
