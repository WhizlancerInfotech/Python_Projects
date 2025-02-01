import hashlib
import json

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(previous_hash='0')

    def create_block(self, previous_hash, vote=None):
        block = {'index': len(self.chain) + 1, 'vote': vote, 'previous_hash': previous_hash}
        block['hash'] = hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()
        self.chain.append(block)
        return block

    def get_last_block(self):
        return self.chain[-1]

blockchain = Blockchain()
vote = input("Enter your vote: ")
blockchain.create_block(previous_hash=blockchain.get_last_block()['hash'], vote=vote)

print(json.dumps(blockchain.chain, indent=4))
