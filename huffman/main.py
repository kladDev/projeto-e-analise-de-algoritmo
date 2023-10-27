from heap_min import HeapMin


def calculate_frequency(data):
    frequency = {}

    for char in data:
        frequency[char] = frequency.get(char, 0) + 1

    return frequency



h = HeapMin()
text = "IFMA CAMPUS CAXIAS"
frequency = calculate_frequency(text)
list_character = h.add_node(frequency)
codes_generate = {}
h.build_huffman_codes(list_character, "", codes_generate)

print(codes_generate)
print(h.compressed_huffman(codes_generate, text))