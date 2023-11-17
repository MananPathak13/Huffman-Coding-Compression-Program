# Huffman-Coding-Compression-Program
This program implements Huffman coding for file compression and decompression in Python. Huffman coding is an efficient method of compressing data without losing any information. This implementation includes two main scripts: encoding.py for compressing (encoding) a file, and decoding.py for decompressing (decoding) the file back to its original form.

**Requirements**
Python 3.x

**Installation**
No installation is required, as the program consists of standalone Python scripts. Ensure that Python 3.x is installed on your system.

**Usage**
To use the Huffman coding compression program, you have two main scripts:

**Encoding**
To compress a file, use the encoding.py script. The script takes an input file and produces a compressed file along with a key file for decompression.
Syntax: python encoding.py <input_file>
This will create two files: <input_file>.huff (the compressed file) and <input_file>.key (the key file needed for decompression).

**Decoding**
To decompress a file, use the decoding.py script. The script requires both the compressed file and its associated key file.
Syntax: python decoding.py <compressed_file> <key_file>
This will produce the decompressed file with the original content.

Example
Given a file example.txt, compress it using:

python encoding.py example.txt
Then, decompress it using:
python decoding.py example.txt.huff example.txt.key

**Contributing**
Contributions to this project are welcome. Please send pull requests or issue reports via GitHub.

**License**
This project is open source and available under the MIT License.
