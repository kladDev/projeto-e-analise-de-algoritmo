class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None


class HeapMin:

    def __init__(self) -> None:
        self.heap = []
        self.level = 0

    def add_node(self, data):
        self.heap = [Node(char, freq) for char, freq in data.items()]
        self.heap.sort(key=lambda x: x.freq)

        while len(self.heap) > 1:
            left_node = self.heap.pop(0)
            right_node = self.heap.pop(0)

            self.level += 1
            merged_node = Node(f'', left_node.freq + right_node.freq)
            merged_node.left = left_node
            merged_node.right = right_node

            self.heap.append(merged_node)
            self.heap.sort(key=lambda x: x.freq)

        return self.heap[0]

    def build_huffman_codes(self, data, code="", codes = {}):
        if data is not None:
            if data.char:
                codes[data.char] = code
                return

            self.build_huffman_codes(data.left, code + "0", codes)
            self.build_huffman_codes(data.right, code + "1", codes)

    def compressed_huffman(self, dictionary, text):
        return "".join(dictionary[char] for char in text)

    def show_nodes(self, node, level=0):
        if node is not None:
            self.show_nodes(node.right, level + 1)
            print('  ' * level + f'{node.char}')
            self.show_nodes(node.left, level + 1)