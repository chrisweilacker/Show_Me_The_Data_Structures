import sys

class TreeNode():

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def huffman_encoding(data):
    char_freq = {}
    for char in data
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    
    tuple_list = []
    for key in char_freq:
        tuple_list.append((key, char_freq[key]))

    sortedList = sorted(tuple_list, lambda t: t[1])
    root = None
    #Build Tree
    while len(sortedList) > 0:
        if len(sortedList) >= 2:
            newLeftNode = TreeNode(sortedList.pop(0))
            newRightNode = TreeNode(sortedList.pop(0))
            topNodeTotal = newLeftNode.value[1] + newRightNode.value[1]
            topNode = TreeNode( ( None, topNodeTotal) ) 
            topNode.left = newLeftNode
            topNode.right = newRightNode
            if (root == None):
                root = topNode
            else:
                newRootTotal = root.value[1] + topNode.value[1]
                newRoot
        else:



def huffman_decoding(data,tree):
    pass

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