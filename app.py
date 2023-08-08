from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/greet', methods=['POST'])
def greet():
    try:
        name = request.form.get('name')

        if not name:
            return jsonify({'error': 'please give a name'}), 400

        return jsonify({'message': 'hello  ' + str(name) + ' have a good day!!!'} ), 200

    except Exception as e:
        return jsonify({'error': 'An error occurred', 'details': str(e)}), 500

@app.route('/ping', methods=['GET'])
def ping():
    try:
        

        return jsonify({'hey':'pong'} ), 200

    except Exception as e:
        return jsonify({'error': 'An error occurred', 'details': str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)

