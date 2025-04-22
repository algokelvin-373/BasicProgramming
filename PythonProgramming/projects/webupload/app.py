import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from PIL import Image
import uuid

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit
app.config['USER_UPLOAD'] = 'user'
app.config['CLOTH_UPLOAD'] = 'cloth'

# Ensure upload directories exist
os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], app.config['USER_UPLOAD']), exist_ok=True)
os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], app.config['CLOTH_UPLOAD']), exist_ok=True)


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
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        # Generate unique filename
        filename = f"user_{uuid.uuid4().hex}.{file.filename.rsplit('.', 1)[1].lower()}"
        user_upload_path = os.path.join(app.config['UPLOAD_FOLDER'], app.config['USER_UPLOAD'])
        filepath = os.path.join(user_upload_path, filename)

        # Save original file
        file.save(filepath)

        # Preprocess user image
        preprocess_user_image(filepath)

        # Create resized version for display
        display_filename = f"display_{filename}"
        display_path = os.path.join(user_upload_path, display_filename)
        resize_image(filepath, display_path)

        return {'status': 'success', 'filename': display_filename}

    return {'status': 'error', 'message': 'Invalid file type'}


@app.route('/upload_cloth', methods=['POST'])
def upload_cloth():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        # Generate unique filename
        filename = f"cloth_{uuid.uuid4().hex}.{file.filename.rsplit('.', 1)[1].lower()}"
        cloth_upload_path = os.path.join(app.config['UPLOAD_FOLDER'], app.config['CLOTH_UPLOAD'])
        filepath = os.path.join(cloth_upload_path, filename)

        # Save original file
        file.save(filepath)

        # Preprocess cloth image
        preprocess_cloth_image(filepath)

        # Create resized version for display
        display_filename = f"display_{filename}"
        display_path = os.path.join(cloth_upload_path, display_filename)
        resize_image(filepath, display_path)

        return {'status': 'success', 'filename': display_filename}

    return {'status': 'error', 'message': 'Invalid file type'}


@app.route('/execute', methods=['POST'])
def execute():
    user_filename = request.form.get('user_filename')
    cloth_filename = request.form.get('cloth_filename')

    if not user_filename or not cloth_filename:
        return redirect(url_for('index'))

    # Remove 'display_' prefix to get original filenames
    original_user = user_filename.replace('display_', '')
    original_cloth = cloth_filename.replace('display_', '')

    # Write to text_pairs.txt for VITON
    with open('text_pairs.txt', 'w') as f:
        f.write(f"{original_user} {original_cloth}\n")

    # Here you would typically call your VITON method
    # For now, we'll just redirect to a result page

    # Generate a result filename (in a real app, this would be from VITON)
    result_filename = f"result_{uuid.uuid4().hex}.jpg"

    return redirect(url_for('show_result', result=result_filename))


@app.route('/result/<result>')
def show_result(result):
    return render_template('result.html', result_image=result)


@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(os.path.join(app.config['UPLOAD_FOLDER'], 'results'), filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)