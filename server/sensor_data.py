import configparser


SENSOR_DATA_FILENAME = "sensor_data.log"


def store_data_from_room(all_sensors_data):

    print(all_sensors_data)

    room_id = all_sensors_data["room_id"]
    temperature_value = all_sensors_data["temperature"]

    logfile = configparser.ConfigParser()
    logfile.read(SENSOR_DATA_FILENAME)
    # logfile.set(str(room_id), 'temperature',  str(temperature_value) )

    if str(room_id) not in logfile.sections():
        logfile.add_section(str(room_id))

    logfile.set(str(room_id), 'temperature', str(temperature_value))

    with open(SENSOR_DATA_FILENAME, 'w') as file_out:
        logfile.write(file_out)

    return "Data stored"


if __name__ == "__main__":
    my_room_data = {
        "room_id": 9000,
        "author": "Tibor",
        "temperature": 100
    }
    store_data_from_room(my_room_data)
