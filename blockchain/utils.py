import hashlib


def calculate_hash(data: bytes) -> str:
    """
    Given bytes data, calculate the SHA256 hash of that data

    :param data: The data to be hashed
    :type data: bytes
    :return: The hash of the data.
    """
    hashed_data = hashlib.sha256(data)
    return hashed_data.hexdigest()
