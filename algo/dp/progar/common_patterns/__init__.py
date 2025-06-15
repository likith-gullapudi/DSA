import heapq
import os

class HuffmanCoding:
    def __init__(self, file_path):
        self.file_path = file_path
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    # Step 1: Calculate frequency of each character
    def calculate_frequency(self, text):
        frequency = {}
        for char in text:
            if char not in frequency:
                frequency[char] = 0
            frequency[char] += 1
        return frequency

    # Step 2: Build priority queue (min-heap)
    def build_heap(self, frequency):
        for key, freq in frequency.items():
            heapq.heappush(self.heap, (freq, key))

    # Step 3: Build Huffman Tree
    def build_tree(self):
        while len(self.heap) > 1:
            freq1, char1 = heapq.heappop(self.heap)
            freq2, char2 = heapq.heappop(self.heap)
            merged = (freq1 + freq2, char1 + char2)
            heapq.heappush(self.heap, merged)

    # Step 4: Assign binary codes to characters
    def build_codes(self):
        root = heapq.heappop(self.heap)
        self._assign_codes_recursive(root, "")

    def _assign_codes_recursive(self, root, current_code):
        if len(root[1]) == 1:
            self.codes[root[1]] = current_code
            self.reverse_mapping[current_code] = root[1]
            return

        self._assign_codes_recursive((root[0] // 2, root[1][:len(root[1]) // 2]), current_code + "0")
        self._assign_codes_recursive((root[0] // 2, root[1][len(root[1]) // 2:]), current_code + "1")

    # Step 5: Encode text into binary format
    def get_encoded_text(self, text):
        encoded_text = ""
        for char in text:
            encoded_text += self.codes[char]
        return encoded_text

    # Step 6: Pad encoded text to make it byte-aligned
    def pad_encoded_text(self, encoded_text):
        extra_padding = 8 - len(encoded_text) % 8
        for _ in range(extra_padding):
            encoded_text += "0"

        padded_info = "{0:08b}".format(extra_padding)
        encoded_text = padded_info + encoded_text
        return encoded_text

    # Step 7: Convert binary string to bytes
    def get_byte_array(self, padded_text):
        if len(padded_text) % 8 != 0:
            print("Error: Encoded text not padded properly")
            exit(0)

        b = bytearray()
        for i in range(0, len(padded_text), 8):
            byte = padded_text[i:i+8]
            b.append(int(byte, 2))
        return b

    # Compress the file
    def compress(self):
        with open(self.file_path, 'r') as file:
            text = file.read()
            text = text.rstrip()

        frequency = self.calculate_frequency(text)
        self.build_heap(frequency)
        self.build_tree()
        self.build_codes()

        encoded_text = self.get_encoded_text(text)
        padded_text = self.pad_encoded_text(encoded_text)

        output_path = self.file_path.split('.')[0] + ".bin"
        with open(output_path, 'wb') as output:
            byte_array = self.get_byte_array(padded_text)
            output.write(byte_array)

        print(f"Compressed file saved at: {output_path}")
        print(f"Original size: {os.path.getsize(self.file_path)} bytes")
        print(f"Compressed size: {os.path.getsize(output_path)} bytes")
        return output_path

    # Decompress the file
    def decompress(self, input_path):
        with open(input_path, 'rb') as file:
            bit_string = ""
            byte = file.read(1)
            while byte:
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bit_string += bits
                byte = file.read(1)

        padded_info = bit_string[:8]
        extra_padding = int(padded_info, 2)
        bit_string = bit_string[8:]  # remove padding info
        encoded_text = bit_string[:-extra_padding]  # remove extra padding

        decompressed_text = self.decode_text(encoded_text)

        output_path = input_path.split('.')[0] + "_decompressed.txt"
        with open(output_path, 'w') as output:
            output.write(decompressed_text)

        print(f"Decompressed file saved at: {output_path}")
        return output_path

    # Decode binary text back to original text
    def decode_text(self, encoded_text):
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_mapping:
                character = self.reverse_mapping[current_code]
                decoded_text += character
                current_code = ""

        return decoded_text


# Example Usage
file_path = "now.txt"  # Provide your file path
huffman = HuffmanCoding(file_path)
compressed_file = huffman.compress()
huffman.decompress(compressed_file)
