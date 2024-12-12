import heapq
import binary_data_handler

class Node:
    def __init__(self, frequency, symbol, left=None, right=None):
        self.frequency = frequency
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huffman_direction = ''

    def __lt__(self, nxt):
        return self.frequency < nxt.frequency

huffman_codes = {}

def get_compressed_image(image_bit_string):
    compressed_image_bit_string = ""
    for i in range(0, len(image_bit_string), 8):
        byte = image_bit_string[i:i + 8]
        compressed_image_bit_string += huffman_codes.get(byte, "")
    return compressed_image_bit_string

def calculate_huffman_codes(node, code=''):
    code += node.huffman_direction
    if node.left:
        calculate_huffman_codes(node.left, code)
    if node.right:
        calculate_huffman_codes(node.right, code)
    if not node.left and not node.right:
        huffman_codes[node.symbol] = code

def get_merged_huffman_tree(byte_to_frequency):
    huffman_tree = [Node(frequency, byte) for byte, frequency in byte_to_frequency.items()]
    heapq.heapify(huffman_tree)
    while len(huffman_tree) > 1:
        left = heapq.heappop(huffman_tree)
        right = heapq.heappop(huffman_tree)
        left.huffman_direction = "0"
        right.huffman_direction = "1"
        merged_node = Node(left.frequency + right.frequency, None, left, right)
        heapq.heappush(huffman_tree, merged_node)
    return huffman_tree[0]

def get_frequency(image_bit_string):
    byte_to_frequency = {}
    for i in range(0, len(image_bit_string), 8):
        byte = image_bit_string[i:i + 8]
        byte_to_frequency[byte] = byte_to_frequency.get(byte, 0) + 1
    return byte_to_frequency

def compress(image_bit_string):
    byte_to_frequency = get_frequency(image_bit_string)
    merged_huffman_tree = get_merged_huffman_tree(byte_to_frequency)
    calculate_huffman_codes(merged_huffman_tree)
    binary_data_handler.save_data(huffman_codes, "./IO/Outputs/huffman_codes.txt", 'dictionary')
    return get_compressed_image(image_bit_string)


def decompress(compressed_image_bit_string):
    # Load Huffman codes from the saved file
    huffman_codes = binary_data_handler.load_huffman_codes("./IO/Outputs/huffman_codes.txt")

    # Reverse the dictionary to map codes back to bytes
    code_to_byte = {code: byte for byte, code in huffman_codes.items()}

    decompressed_image_bit_string = ""
    current_code = ""

    # Iterate through the compressed bit string
    for bit in compressed_image_bit_string:
        current_code += bit

        # Check if the current code corresponds to a byte
        if current_code in code_to_byte:
            decompressed_image_bit_string += code_to_byte[current_code]
            current_code = ""  # Reset the code buffer

    return decompressed_image_bit_string
