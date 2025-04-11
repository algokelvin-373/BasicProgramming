import time

from rembg import remove

start = int(time.time() * 1000)
index = 0
while index < 30:
    input_path = f'D:/INA17Group/0S_ServerIna17/photos_result/photos{index + 1}.jpg'
    output_path = f'D:/INA17Group/0S_ServerIna17/photos_result/'
    if index > 99:
        output_path += f'50{index}_00.jpg'
    elif 10 <= index <= 99:
        output_path += f'500{index}_00.jpg'
    else:
        output_path += f'5000{index}_00.jpg'

    # Read Input Image and Remove Background
    with open(input_path, 'rb') as i:
        input_data = i.read()
        output_data = remove(input_data)

    # Write Data Image After Remove Background
    with open(output_path, 'wb') as o:
        o.write(output_data)

    index += 1
end = int(time.time() * 1000)

print(f'Done - Time: {end - start} ms') # milidetik