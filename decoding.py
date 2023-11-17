import heapq

def read_frequency_file(filename):
    frequencies = {}
    with open(filename, "r") as freq_file:
        for line in freq_file:
            char, freq = line.strip().split(": ")
            frequencies[char] = int(freq)
    return frequencies

def build_huffman_tree_from_frequencies(frequencies):
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

def decode_text(encoded_text, huffman_tree):
    decoded_text = ""
    current_code = ""
    for bit in encoded_text:
        current_code += bit
        for char, code in huffman_tree:
            if code == current_code:
                decoded_text += char
                current_code = ""
                break
    return decoded_text

# Read Huffman codes from codes.txt
huffman_codes = {}
with open("codes.txt", "r") as codes_file:
    for line in codes_file:
        char, code = line.strip().split(": ")
        huffman_codes[code] = char

# Read compressed binary data from compressed.bin
with open("compressed.bin", "rb") as compressed_file:
    byte_data = compressed_file.read()
    encoded_text = ''.join(format(byte, '08b') for byte in byte_data)

# Read frequencies from frequency.txt and build Huffman tree
frequencies = read_frequency_file("frequency.txt")
huffman_tree = build_huffman_tree_from_frequencies(frequencies)

# Decode the text
decoded_text = decode_text(encoded_text, huffman_tree)

# Perform transformations (lowercase, whitespace replacement)
decoded_text = decoded_text.lower().replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')

# Write decoded text to decoded.txt
with open("decoded.txt", "w") as decoded_file:
    decoded_file.write(decoded_text)

print("Decoding complete.")
