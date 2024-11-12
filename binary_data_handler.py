import os
import json

def read_image_bit_string(image_path):
    bit_string = []
    with open(image_path, 'rb') as image:
        while (byte := image.read(1)):
            byte_value = ord(byte)
            bits = bin(byte_value)[2:].rjust(8, '0')
            bit_string.append(bits)
    return ''.join(bit_string)


def load_huffman_codes(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def save_data(data, save_path, data_type):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    if data_type == 'image':
        with open(save_path, 'wb') as file:
            byte_array = bytearray(
                int(data[i:i + 8], 2) for i in range(0, len(data), 8)
            )
            file.write(byte_array)
    elif data_type == 'dictionary':
        with open(save_path, 'w') as file:
            json.dump(data, file)
    else:
        raise ValueError("Invalid data_type. Supported values: 'image', 'dictionary'")