#Show Me The Data Structures

##1. LRU Cache
This creates an LRU Cache that has O(1) time retrieving and setting new items.  My implementation of the LRU Cache uses a 
linkedlist to keep track of the keys that were created and when they were accessed and places the nodes that holds the values 
in both a dictionary with the keys as well as the linkedlist.  I realized after implementation I could have used a tuple instead
of creating a new class definiton for holding both the key and value inside the linkedlist.

##2. File Recursion
My file recursion implementation is O(n) time as it must loop through each of the files in the specified folder. 
It handles user input errors on folder path by utilizing a try catch block.

##3. Huffman Coding
This algorithm creates a tree from a string and is O(n) as we need to run through the input several times first 
to build the tree second to create the codes and finally to convert the string into binary in order to encode the string.
Again the decode is also O(n) as it needs to go through each digit in the encoded string and go through the tree to decode.
The space complexity here is actually smaller as we do compress it and especially in a large string like a book you would be
limited maybe to 87 characters after which the tree would not be getting any larger.

##4. Active Directory
This algorithm recursively checks the tree and has a worst case of O(n).  I implemented a check to stop an infinite loop on the function
I wrote.  I think an even better implementation would be in the append group function but as the code was given to me didnt want to change it.

##5. Blockchain
This is simply a linkedList that also has a verification because each node has previous hash key so that the Blockchain can be verified.
Inserting a new block is an O(1) operation but reading a block has a worst case of O(n).

##6. Union and Intersion of Two Linked Lists
My implementation has an O(n) time complexity as I build one or two sets depending on the problem then return the set in union or use the difference
operation for sets in the intersection implementation.


