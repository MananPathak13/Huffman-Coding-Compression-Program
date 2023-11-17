import heapq
import os

def calculate_frequencies(text):
    frequencies = {}
    for char in text:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    return frequencies

def build_huffman_tree(frequencies):
    heap = [[weight, [char, ""]] for char, weight in frequencies.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

def generate_huffman_codes(tree):
    huffman_codes = {}
    for char, code in tree:
        huffman_codes[char] = code
    return huffman_codes

def encode_text(text, huffman_codes):
    encoded_text = ""
    for char in text:
        encoded_text += huffman_codes[char]
    return encoded_text

def write_output_files(frequencies, huffman_codes, encoded_text):
    with open("frequency.txt", "w") as freq_file:
        for char, freq in frequencies.items():
            freq_file.write(f"{char}: {freq}\n")

    with open("codes.txt", "w") as codes_file:
        for char, code in huffman_codes.items():
            codes_file.write(f"{char}: {code}\n")

    with open("compressed.bin", "wb") as compressed_file:
        padded_encoded_text = encode_text_padded(encoded_text)
        byte_array = bytearray()
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i + 8]
            byte_array.append(int(byte, 2))
        compressed_file.write(bytes(byte_array))

def encode_text_padded(encoded_text):
    extra_padding = 8 - len(encoded_text) % 8
    encoded_text += '0' * extra_padding
    padded_info = format(extra_padding, '08b')
    padded_encoded_text = padded_info + encoded_text
    return padded_encoded_text

# Read input text from a file
input_filename = input("Enter the input filename: ")
with open(input_filename, "r") as input_file:
    text = input_file.read()

# Step 1: Calculate frequencies
frequencies = calculate_frequencies(text)

# Step 2: Build the Huffman Tree
huffman_tree = build_huffman_tree(frequencies)

# Step 3: Generate Huffman codes
huffman_codes = generate_huffman_codes(huffman_tree)

# Step 4: Encode the text
encoded_text = encode_text(text, huffman_codes)

# Step 5: Write output files
write_output_files(frequencies, huffman_codes, encoded_text)

print("Encoding complete.")
