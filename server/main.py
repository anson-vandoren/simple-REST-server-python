from flask import Flask, jsonify

app = Flask(__name__)

motor_position = 0
motor_increment = 1
motor_max = 360

@app.route('/')
def hello_world():
    return 'Hello, World'

@app.route('/rotate/<direction>', methods=['POST'])
def rotate_cmd(direction):
    print(f'received command to rotate in {direction} direction')
    if direction == "positive":
        motor_position += motor_increment
    elif direction == "negative":
        motor_position -= motor_increment
    else:
        return "Invalid direction", 400
    if motor_position >= 360:
        motor_position -= 360
    if motor_position < 0:
        motor_position += 360
    return {'motor_status': 'OK', 'motor_position': motor_position}

@app.route('/status', methods=['GET'])
def get_status():
    return {'motor_status': 'OK', 'motor_position': motor_position}
