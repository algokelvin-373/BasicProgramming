import os
from datetime import datetime

from PIL import Image
from flask import Flask, render_template, request, redirect, url_for, send_from_directory

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'datasets'
app.config['TEST_CLOTH'] = 'test/cloth'
app.config['TEST_IMAGE'] = 'test/image'

# Ensure upload directories exist
os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], app.config['TEST_CLOTH']), exist_ok=True)
os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], app.config['TEST_IMAGE']), exist_ok=True)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}


def resize_image(image_path, output_path, scale=0.5):
    with Image.open(image_path) as img:
        width, height = img.size
        new_size = (int(width * scale), int(height * scale))
        resized_img = img.resize(new_size, Image.Resampling.LANCZOS)
        resized_img.save(output_path)


def preprocess_user_image(image_path):
    """Preprocessing steps 1-4 for user image"""
    # Implement your preprocessing steps 1-4 here
    pass


def preprocess_cloth_image(image_path):
    """Preprocessing step 5 for cloth image"""
    # Implement your preprocessing step 5 here
    pass


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload_user', methods=['POST'])
def upload_user():
    if 'file' not in request.files:
        return {'status': 'error', 'message': 'No file selected'}, 400

    file = request.files['file']
    if file.filename == '':
        return {'status': 'error', 'message': 'No file selected'}, 400

    if file and allowed_file(file.filename):
        timestamp = datetime.now().strftime("%H%M%S")
        filename = f"50001{timestamp}_00.jpg"
        user_path = os.path.join('datasets', 'test', 'image')
        filepath = os.path.join(user_path, filename)

        # Save the file
        file.save(filepath)

        return {
            'status': 'success',
            'filename': filename,
            'display_path': f"/datasets/test/image/{filename}"
        }

    return {'status': 'error', 'message': 'Invalid file type'}, 400


@app.route('/upload_cloth', methods=['POST'])
def upload_cloth():
    if 'file' not in request.files:
        return {'status': 'error', 'message': 'No file selected'}, 400

    file = request.files['file']
    if file.filename == '':
        return {'status': 'error', 'message': 'No file selected'}, 400

    if file and allowed_file(file.filename):
        # Get original filename without extension
        original_name = os.path.splitext(file.filename)[0]
        ext = os.path.splitext(file.filename)[1].lower()

        # Save with original filename
        filename = f"{original_name}{ext}"
        cloth_path = os.path.join(app.config['UPLOAD_FOLDER'], app.config['TEST_CLOTH'])
        filepath = os.path.join(cloth_path, filename)

        # Save original file
        file.save(filepath)

        # Preprocess cloth image
        preprocess_cloth_image(filepath)

        return {
            'status': 'success',
            'filename': filename,
            'display_path': f"/{cloth_path}/{filename}"
        }

    return {'status': 'error', 'message': 'Invalid file type'}, 400


@app.route('/execute', methods=['POST'])
def execute():
    # Get the filenames from the form
    user_filename = request.form.get('user_filename')
    cloth_filename = request.form.get('cloth_filename')

    if not user_filename or not cloth_filename:
        return redirect(url_for('index'))

    # Define the paths
    test_pairs_path = os.path.join('datasets', 'test_pairs.txt')
    user_image_path = os.path.join('datasets', 'test', 'image', user_filename)
    cloth_image_path = os.path.join('datasets', 'test', 'cloth', cloth_filename)

    # Write to test_pairs.txt in the required format
    with open(test_pairs_path, 'w') as f:
        f.write(f"{user_filename} {cloth_filename}\n")

    # Here you would typically call your VITON processing
    # result_filename = process_viton(user_image_path, cloth_image_path)

    # For now, we'll just use a placeholder result
    result_filename = "result_example.jpg"

    return redirect(url_for('show_result', result=result_filename))

@app.route('/datasets/<path:filename>')
def datasets_files(filename):
    return send_from_directory(os.path.join(app.config['UPLOAD_FOLDER']), filename)

@app.route('/result/<result>')
def show_result(result):
    return render_template('result.html', result_image=result)


@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(os.path.join(app.config['UPLOAD_FOLDER'], 'results'), filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)