import hashlib
import time
import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      
    def calc_hash(self):
      sha = hashlib.sha256()
      theString = f'Time: {self.timestamp}'
      hash_str = theString.encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()

class BlockChainNode:
  def __init__(self, block):
    self.value = block
    self.next = None

class BlockChain:
  def __init__(self):
    self.head = None
    self.tail = None

  def append(self, data):
    if self.head == None:
      newBlock = Block( datetime.datetime.now().timestamp(), data, None)
      self.head = BlockChainNode(newBlock)
      self.tail = self.head
    else:
      newBlock = Block(datetime.datetime.now().timestamp(), data, self.tail.value.hash)
      self.tail.next = BlockChainNode(newBlock)
      self.tail = self.tail.next

myBlockChain = BlockChain()

myBlockChain.append('Bought a bitcoin')
time.sleep(1)
myBlockChain.append('Holding my bitcoin')
time.sleep(1)
myBlockChain.append('Selling my bitcoin')
time.sleep(1)
myBlockChain.append(None)
time.sleep(1)
myBlockChain.append(45389765421)


currentBlockNode = myBlockChain.head
blockNumber = 1 
while currentBlockNode:
  currentBlock = currentBlockNode.value
  print(f'Block Number: {blockNumber}')
  print(f'Previous Hash: {currentBlock.previous_hash}')
  print(f'Hash: {currentBlock.hash}')
  print(f'Time: {currentBlock.timestamp}')
  print(f'Data: {currentBlock.data}')
  currentBlockNode = currentBlockNode.next
  blockNumber += 1