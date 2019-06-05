import sys

class TreeNode():

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def huffman_encoding(data):
    char_freq = {}
    for char in data:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    
    tuple_list = []
    for key in char_freq:
        tuple_list.append((key, char_freq[key]))

    sortedList = sorted(tuple_list, key = lambda t: t[1])


    def createCharDict(node, bitstring='', charDict={}):
        if (node.value[0] != None):
            charDict[node.value[0]] = bitstring
        
        if node.left:
            createCharDict(node.left, bitstring + '0', charDict)
        
        if node.right:
            createCharDict(node.right, bitstring + '1', charDict)

        return charDict


    def buildTreeFromSorted(sortedList):
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
                    newRootNode = TreeNode( (None, newRootTotal) )
                    newRootNode.left = topNode
                    newRootNode.right = root
                    root = newRootNode
            else:
                newLeftNode = TreeNode(sortedList.pop(0))
                topNode = TreeNode( ( None, newLeftNode.value[1]) ) 
                topNode.left = newLeftNode
                if (root == None):
                    root = topNode
                else:
                    newRootTotal = root.value[1] + topNode.value[1]
                    newRootNode = TreeNode( (None, newRootTotal) )
                    newRootNode.left = topNode
                    newRootNode.right = root
                    root = newRootNode
        return root
    
    root = buildTreeFromSorted(sortedList)
        
    charDict = createCharDict(root)
    encodedDataString = '1'

    for char in data:
        encodedDataString += charDict[char]
    
    return int(encodedDataString, base=2), root
    

def huffman_decoding(data,tree):
    encodedDataString = bin(data)[3:]
    decodedString = ''
    currentNode = tree

    for binary in encodedDataString:
        if binary == '0':
            currentNode = currentNode.left
        else:
            currentNode = currentNode.right
        
        if currentNode.value[0] != None:
            decodedString += currentNode.value[0]
            currentNode = tree
    return decodedString

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(encoded_data)))
    print ("The content of the encoded data is: {0:b}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))

    a_great_sentence = "This is a much larger sentence that should have a much larger compression amount due to the fact that we have a lot of repeated characters and there are only about 80 or so characters when including capitals lowercase and punctuation that it could be so we should see a much larger compresion amount this time around."

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(encoded_data)))
    print ("The content of the encoded data is: {0:b}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))