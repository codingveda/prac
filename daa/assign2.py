"""
https://www.programiz.com/dsa/huffman-coding
"""

# Huffman Coding in python
string="ffdbaeedaffffbcccefbcfdfdffefebdfffeffffefcdefeedefdfcbeebddcffdacffeadfcefcbfffcfffbffdfaffffbcfeff"

# Creating tree nodes
class NodeTree():

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

# Main function implementing huffman coding
def huffman_code_tree(node, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, binString + '0'))
    d.update(huffman_code_tree(r, binString + '1'))
    return d

# Calculating frequency
freq = {}
for c in string:
    freq[c] = freq.get(c, 0) + 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
print(freq)
nodes = freq
while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes.pop()
    nodes.pop()
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])

print("character" + "        " + "code")
for key in huffmanCode:
    print("    " + key + "     --->   " + huffmanCode[key])