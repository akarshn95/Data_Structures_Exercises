"""
References :
- GeeksForGeeks
- Programiz
"""

import sys
import heapq
    
class Huff_Node:
    def __init__(self,value, wt):
        """Create node for given symbol and weight."""
        self.left = None
        self.right = None
        self.value = value
        self.wt = wt        
        
    def __lt__(self, other):
        return self.wt < other.wt
    
def get_frequecies(data):
    freq = {}
    
    for item in data:
        if item not in freq:
            freq[item] = 1
        freq[item] +=1
    # make the dictionary into an list array which is sorted on values
    freq_sorted = sorted(zip(freq.values(), freq.keys()))

    for i in range(len(freq_sorted)):
        value = freq_sorted[i][1] # value
        freq = freq_sorted[i][0] # frequency
        # converting to an array of nodes which have the value and frequency of the characters
        freq_sorted[i] = Huff_Node(value, freq)  

    return freq_sorted  

def huffman_tree(data):
    # building a Huffman tree
    heap = get_frequecies(data) 
    heapq.heapify(heap) 
    while len(heap) != 1:
        h_node = Huff_Node(None,None)
        left = heapq.heappop(heap)
        h_node.left  = left
        right = heapq.heappop(heap)
        h_node.right  = right
        h_node.wt = left.wt + right.wt     # popped the first two nodes of least value and added a node whose weight is sum of the two popped nodes
        heapq.heappush(heap, h_node)
    return heap

# Referred from Tutorials Point Huffman algorithm section
def create_Huffcode_table(root):
    code = {}
    # a left edge represents a 0 bit, a right edge represents a 1 bit
    def getCode(hNode, currentCode=""):
        if (hNode == None): 
            return
        if (hNode.left == None and hNode.right == None):
            code[hNode.value] = currentCode
        getCode(hNode.left, currentCode + "0")
        getCode(hNode.right, currentCode + "1")
    getCode(root[0])
    return code


def huff_encode(data):
   
    if(len(get_frequecies(data))) == 1:
        return "0"*len(data)
    huff_code = "" 
    root = huffman_tree(data)
    table = create_Huffcode_table(root)
    for item in data:
        huff_code += table[item]
    return huff_code


def huffman_decode(string,root):
    
    if(len(get_frequecies(string))) == 1:
        return len(string)*str(root.value)
    decode = ""
    n = len(string)
    count = 0
    while count < n:
        current = root[0]
        while current.left != None and current.right != None:
            if string[count] == "0":
                current = current.left
            else:
                current = current.right
            count+=1
        decode+=current.value
    return decode

def huffman_encoding(data):
    return huff_encode(data), huffman_tree(data)
  

def huffman_decoding(data,tree):
    return huffman_decode(data,tree)



if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
