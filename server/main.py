from flask import Flask, request, jsonify
import sensor_data

app = Flask(__name__)


@app.route('/room/<room_id>', methods=['GET'])
def get_data_for_room_id(room_id):
    print("GET request for room_id: ", room_id)
    odpoved = sensor_data.load_data_from_room(room_id)

    return jsonify(odpoved), 200


@app.route('/sensor', methods=['POST'])
def sensor():
    data = request.get_json()
    print(data)
    sensor_data.store_data_from_room(data)
    return "Ok", 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

