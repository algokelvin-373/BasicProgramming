from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


# Route for main page
@app.route('/')
def home():
    return render_template('index.html')


# Route for API will be hit oleh button
@app.route('/api/data', methods=['GET', 'POST'])
def get_data():
    if request.method == 'POST':
        # Proses data is sent from frontend if any
        data = request.json or request.form
        print("Data received:", data)

    # Example response data
    response_data = {
        'status': 'success',
        'message': 'Data berhasil diambil dari API',
        'items': [
            {'id': 1, 'name': 'Item 1'},
            {'id': 2, 'name': 'Item 2'},
            {'id': 3, 'name': 'Item 3'}
        ]
    }
    return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=True)