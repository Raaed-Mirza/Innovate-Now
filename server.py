from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    name = data['name']
    email = data['email']

    # Process the data or perform any backend tasks
    # ...

    # Return a response back to the frontend
    response = {
        "status": "success",
        "message": "Data received successfully!"
    }

    return jsonify(response)
    
if __name__ == '__main__':
    app.run()
