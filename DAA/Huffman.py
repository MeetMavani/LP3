class NodeTree:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def __str__(self):
        return f'{self.left}_{self.right}'

def huffman_code_tree(node, binString=''):
    # Base case: leaf node
    if isinstance(node, str):
        return {node: binString}
    # Recursive case: internal node
    l, r = node.children()
    d = {}
    d.update(huffman_code_tree(l, binString + '0'))
    d.update(huffman_code_tree(r, binString + '1'))
    return d

# Step 1: Calculate frequency of each character
string = 'BCAADDDCCACACAC'
freq = {}
for char in string:
    freq[char] = freq.get(char, 0) + 1

# Step 2: Sort characters by frequency
nodes = sorted(freq.items(), key=lambda x: x[1], reverse=True)

# Step 3: Build the Huffman tree
while len(nodes) > 1:
    (key1, c1) = nodes.pop()
    (key2, c2) = nodes.pop()
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

# Step 4: Generate Huffman codes
huffmanCode = huffman_code_tree(nodes[0][0])

# Print the codes
print(' Char | Huffman code ')
print('----------------------')
for char, _ in freq.items():
    print(f' {char!r:4} | {huffmanCode[char]:12}')
