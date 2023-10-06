from heap_min import HeapMin


def calculate_frequency(data):
    frequency = {}

    for char in data:
        frequency[char] = frequency.get(char, 0) + 1

    return frequency



h = HeapMin()
text = "aaatttttjooooooopp"
t = calculate_frequency(text)
nodes = h.add_node(t)
# print(h.build_huffman_tree())
h.show_nodes(nodes)
# h.add_node()