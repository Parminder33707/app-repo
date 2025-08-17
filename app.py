from flask import Flask, request, jsonify

app = Flask(__name__)

workouts = []//test

@app.route('/log_workout', methods=['POST'])
def log_workout():
    data = request.json
    if data:
        workouts.append(data)
        return jsonify({"message": "Workout logged!", "data": data}), 201
    return jsonify({"error": "No data"}), 400

@app.route('/get_workouts', methods=['GET'])
def get_workouts():
    return jsonify(workouts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
