from rembg import remove
import time as time

# Read Image
times = time.time()
input_path = "D:/test10.jpg"
output_path = f"D:/output_no_bg_{times}.jpg"

# Delete background
with open(input_path, 'rb') as f:
    image = f.read()
output = remove(image)  # Result JPG without background

# Save result
with open(output_path, 'wb') as f:
    f.write(output)