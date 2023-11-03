from flask import Flask, jsonify, request

app = Flask(__name__)

weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}

@app.route('/weather/<string:city>', methods=['GET'])
def get_weather(city):
    if city in weather_data:
        return jsonify(weather_data[city]), 200
    else:
        return "City not found", 404

@app.route('/weather', methods=['POST'])
def create_weather():
    data = request.get_json()
    if 'city' in data and 'temperature' in data and 'weather' in data:
        city = data['city']
        weather_data[city] = {'temperature': data['temperature'], 'weather': data['weather']}
        return "Weather data created", 201
    else:
        return "Invalid data format", 400

@app.route('/weather/<string:city>', methods=['PUT'])
def update_weather(city):
    if city in weather_data:
        data = request.get_json()
        if 'temperature' in data:
            weather_data[city]['temperature'] = data['temperature']
        if 'weather' in data:
            weather_data[city]['weather'] = data['weather']
        return "Weather data updated", 200
    else:
        return "City not found", 404

@app.route('/weather/<string:city>', methods=['DELETE'])
def delete_weather(city):
    if city in weather_data:
        del weather_data[city]
        return "Weather data deleted", 204
    else:
        return "City not found", 404

if __name__ == '__main__':
    app.run(debug=True)
