"""
Based on:
 - https://medium.com/coinmonks/python-tutorial-build-a-blockchain-713c706f6531
"""
import hashlib
import orjson
from time import time


class BlockChain(object):
    """
    Create a new BlockChain class. A BlockChain contains a chain of blocks, as
    wll as the methods to add new blocks.
    """

    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        # Create initial block
        self.new_block(
            previous_hash="Hello World !",
            proof=100
        )

    def new_block(self, proof, previous_hash=None):
        """
        Create a new block and add it to the chain

        :param proof: The proof given by the Proof of Work algorithm
        :param previous_hash: This is the hash of the previous block
        :return: The new block itself.
        """

        # Create a new block
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        # Empty the pending transactions
        self.pending_transactions = []

        # Add the block to the chain
        self.chain.append(block)
        return block

    @property
    def last_block(self):
        """
        Return the last block in the chain
        :return: The last block in the chain.
        """
        return self.chain[-1]

    def new_transaction(self, sender, recipient, amount) -> int:
        """
        Create a new transaction object and add it to the list of pending transactions

        :param sender: The sender of the coins
        :param recipient: The recipient of the coins
        :param amount: The amount of the transaction. This is a floating point number
        :return: The index of the block that will hold this transaction
        """

        # Create a new transaction object
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }

        # Add to the pending transactions
        self.pending_transactions.append(transaction)

        # Return its index
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """
        Given a block, convert it to bytes and hash it

        :param block: The block to hash
        :return: The hash of the block.
        """

        # Convert the block to bytes
        bytes_block: bytes = orjson.dumps(block, option=orjson.OPT_SORT_KEYS)

        # Hash
        raw_hash = hashlib.sha256(bytes_block)
        hex_hash = raw_hash.hexdigest()
        return hex_hash
