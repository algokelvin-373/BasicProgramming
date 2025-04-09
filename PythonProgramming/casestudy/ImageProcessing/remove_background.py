from rembg import remove

input_path = 'D:/AlgoKelvin/My_Project/Februari 2025/BasicProgramming/PythonProgramming/casestudy/ImageProcessing/photos/photos5.jpg'
output_path = 'D:/AlgoKelvin/My_Project/Februari 2025/BasicProgramming/PythonProgramming/casestudy/ImageProcessing/photos/output_photos5.jpg'

# Read Input Image and Remove Background
with open(input_path, 'rb') as i:
    input_data = i.read()
    output_data = remove(input_data)

# Write Data Image After Remove Background
with open(output_path, 'wb') as o:
    o.write(output_data)

print('Success remove background')