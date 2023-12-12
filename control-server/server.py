from flask import Flask, jsonify, request
from weather import Weather
import logging

logging.basicConfig(filename='module.log', level=logging.DEBUG)

app = Flask(__name__);

# section: Weather
@app.route('/weather/<city>/<period>', methods = ['GET'])
def weather(city, period):
    if period not in ["current", "morning"]:
        logging.debug(f"Invalid period. Choose 'current' or 'morning', data : {period}")
        return jsonify({"error": "Invalid period. Choose 'current' or 'morning'."}), 400

    city = str(city).capitalize()
    weather = Weather(city)

    data = weather.get_temp(period)
    
    if data is None:
        logging.debug(f"data is None : {data}")
        return jsonify({ "error": "Failed to fetch weather data." }), 500
    elif data == 404:
        logging.error(f"request status {data}!")
        return jsonify({ "error": "Failed to request, please check parameter." }), data
    return jsonify(data)

# section Database




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')