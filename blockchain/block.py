from time import time
from typing import Optional
import orjson
from .utils import calculate_hash


class Block:

    def __init__(
            self,
            transaction_data: str,
            timestamp: float = time(),
            previous_block: Optional["Block"] = None
    ):
        self.transaction_data = transaction_data
        self.timestamp: float = timestamp
        self.previous_block: Optional["Block"] = previous_block

    @property
    def previous_block_hash(self) -> str:
        """
        Return the hash of the previous block in the chain
        :return: The hash of the previous block
        """

        if self.previous_block:
            return self.previous_block.hash
        return ""

    @property
    def hash(self) -> str:
        """
        Transforms the block's data into bytes and calculates its hash.
        :return: The hash of the block.
        """

        # Transform block's data to bytes
        bytes_block: bytes = orjson.dumps({
            "transaction_data": self.transaction_data,
            "timestamp": self.timestamp,
            "previous_block_hash": self.previous_block_hash
        }, option=orjson.OPT_SORT_KEYS)

        # Calculate and return its hash
        return calculate_hash(bytes_block)
