import hashlib
from datetime import datetime

class Block:

    def __init__(self, data, previous_hash):
        self.timestamp = datetime.utcnow()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)
        self.next=None
    
    def calc_hash(self,data):
        sha = hashlib.sha256()
        hash_str = str(self.previous_hash).encode('utf-8')+str(self.timestamp).encode('utf-8')+str(self.data).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()
    
    def __repr__(self):
        return ("Timestamp: "+str(self.timestamp)+"\nData: "+str(self.data)+"\nHash Value: "+str(self.hash)+"\nPrevious Hash: "+str(self.previous_hash)+"\n")
    


class Blockchain(object):
    
    def __init__(self):
        self.head=None
        self.tail=None
        
    def add_block(self,data):
        if self.head is None:
            new_block=Block(data,None)
            self.head=new_block
            self.tail=new_block
        else:
            new_block=Block(data,self.tail.hash)
            self.tail.next=new_block
            self.tail=new_block
            
    def get_blockchain(self):
        node=self.head
        if node is None:
            print("Blockchain is empty")
            return
        while node!=None:
            print(node)
            node=node.next
        return 


# TEST CASES 

# TEST CASE 1
block_chain_1=Blockchain()

block_chain_1.add_block(1)
block_chain_1.add_block(2)
block_chain_1.add_block(3)
block_chain_1.add_block(4)
block_chain_1.add_block(5)

print("\nBLOCKCHAIN 1\n")
block_chain_1.get_blockchain()    #prints the blockchain of 5 blocks

# TEST CASE 2
block_chain_2=Blockchain()

print("\nBLOCKCHAIN 2\n")
block_chain_2.get_blockchain()  #prints that blockchain is empty

# TEST CASE 3
block_chain_3=Blockchain()

block_chain_3.add_block("This")
block_chain_3.add_block("is")
block_chain_3.add_block("a")
block_chain_3.add_block("blockchain")
block_chain_3.add_block("of")
block_chain_3.add_block("strings")

print("\nBLOCKCHAIN 3\n")
block_chain_3.get_blockchain()    #prints the blockchain

