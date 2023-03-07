import hashlib, json
from time import time
from uuid import uuid4
from textwrap import dedent
from flask import Flask, jsonify, request
from urllib.parse import urlparse
import requests


class   Pringlechain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.nodes=set()

        self.new_block(previous_hash='1',proof=100)

    def valid_chain(self, chain):
        # determines chain validity

        last_block= chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            print(f'{last_block}')
            print(f'{block}')
            print("\n---------------\n")

            # checks if hash of block is correct
            if block['previous_hash'] != self.hash(last_block):
                return False
            
            # checks PoW
            if not self.valid_proof(last_block['proof'], block['proof']):
                return False
            
            last_block=block
            current_index += 1

        return True
    
    def resolve_conflicts(self):
        # Consense algorithm to resolve conficts by replacing chain with longest chain in network
        neighbors = self.nodes
        new_chain = None

        max_length = len(self.chain)

        # verify chains from all nodes in network
        for node in neighbors:
            response = requests.get(f'http://{node}/chain')
            
            if response.status_code == 200:
                length = response.json()['length']
                chain=response.json()['chain']

                # Check if length is longer and chain is valid

                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain


        # Replace our current chain with the newly discovered chain if valid and longer than ours
        if new_chain:
            self.chain = new_chain
            return True
        return False



    def register_node(self, address):
        # Add new node to nodelist

        parsed_url = urlparse(address)
        if parsed_url.netloc:
            self.nodes.add(parsed_url.netloc)
        elif parsed_url.path:
            # Accepts an URL without scheme like '192.168.0.5:5000'.
            self.nodes.add(parsed_url.path)
        else:
            raise ValueError('Invalid URL')
        

    def proof_of_work(self, last_proof):

        proof = 0 
        while self.valid_proof(last_proof, proof) is False:
            proof +=1
        
        return proof
    
    def valid_proof(self, last_proof, proof):
        """Validates the proof provided"""

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == '0000'
    
    def new_block(self, proof, previous_hash=None):
        #This will create new blocks and add it to the blockchain

        block = {
            'index': len(self.chain)+1,
            'timestamp': time(),
            "transactions" : self.current_transactions,
            'proof' : proof,
            'previous_hash' : previous_hash or self.hash(self.chain[-1])


        }

        # Reset current list of transactions to be transcribed to next new block
        self.current_transactions = []

        self.chain.append(block)
        return block
    


    

    def new_transaction(self, sender, recipient, amount):
        #Defines a new transaction and adds to the list of transactions 
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        
        return self.last_block['index']+1

    @property
    def last_block(self):
        return self.chain[-1]
    
    @staticmethod
    def hash(block):
        # Hashes a block instance
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


  


# Get the party started
app = Flask(__name__)

# Unique address for node
node_identifier = str(uuid4()).replace('-','')

pringlechain = Pringlechain()

@app.route('/mine', methods=['GET'])
def mine():
    #run PoW algorithm for next proof
    last_block = pringlechain.last_block
    last_proof = last_block['proof']
    proof = pringlechain.proof_of_work(last_proof)
    #rewards distributed for popping the top on the new block will be a '0'
    pringlechain.new_transaction(
        sender='0',
        recipient=node_identifier,
        amount = 1
    )

    #Add new block to chain
    previous_hash = pringlechain.hash(last_block)
    block=pringlechain.new_block(proof, previous_hash)

    response = {
        'message':'New top popped',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof':block['proof'],
        'previous_hash': block['previous_hash'],
    }

    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    #Checks for required fields
    required = ['sender', 'recipient', 'amount']
    if not all(x in values for x in required):
        return 'Missing required values', 400
    index = pringlechain.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message': f'Transaction will be added to Pringle{index}'}
    return jsonify(response),201

"""
Test JSON because I am super lazy
{
    "sender" : "1935ca905c824d2b9a7e3c0173389447",
    "recipient" : "Jessie",
    "amount" : "1"
}

"""

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': pringlechain.chain,
        'length': len(pringlechain.chain)
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    print('registering')
    values=request.get_json()

    nodes=values.get('nodes')
    print(nodes)
    if nodes is None:
        return "Error: please input a valid listing of nodes", 400
    
    for node in nodes:
        pringlechain.register_node(node)

    response = {
        'message': 'New pringles can has been added',
        'total_nodes':list(pringlechain.nodes),

    }
    return jsonify(response), 201


@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = pringlechain.resolve_conflicts()

    if replaced:
        response = {
            'message':'Our pringle can has been replaced',
            'new_chain': pringlechain.chain

        }
    
    else:
        response = {
            'message' : 'Our Pringle can is the one',
            'chain':pringlechain.chain

        }

    return jsonify(response), 200

