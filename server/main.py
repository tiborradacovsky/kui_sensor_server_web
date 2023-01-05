from flask import Flask, request
import sensor_data

app = Flask(__name__)


@app.route('/sensor', methods=['POST'])
def sensor():
    data = request.get_json()
    print(data)
    sensor_data.store_data_from_room(data)
    return "Ok", 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

