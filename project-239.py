import hashlib
import json
from time import time

chain = []
def block(proof, previous_hash = None):
    transaction = {
        "Sender": "Miku",
        "Recipient": "Miku2",
        "Amount": "5ETH"
    }
    data = {
        "block height": 1 , 
        "timestamp": time(),
        "transactions": transaction,
        "Block Reward": '2.51335502599523068 Ether (2 + 0.45085502599523068 + 0.0625)', 
        "Uncle Reward": '1.75 ether', 
        "Difficulty": "7,289,333,444,555,444",
        "Total Difficulty": "7,289,333,444,555,444",
        "Size": "66,736bytes", 
        "Proof" : proof,
        "previous_hash" : previous_hash,
    }
    chain.append(data)
    print("Block information: ", data)
    stringobj = json.dumps(data)
    blockstring = stringobj.encode()
    raw_hash = hashlib.sha512(blockstring)
    hex_hash = raw_hash.hexdigest()
    print("Hash code of block: ", hex_hash)

block(previous_hash= "No previous hash", proof=000)