import hashlib

def generate_hash(data):
    """
    Generate a SHA-256 hash for the given data.

    :param data: The string data to hash.
    :return: The hexadecimal representation of the hash.
    """
    if not isinstance(data, str):
        raise TypeError("Data must be a string")
    
    # Encode the string data to bytes
    data_bytes = data.encode('utf-8')
    
    # Generate the SHA-256 hash
    hash_object = hashlib.sha256(data_bytes)
    
    # Return the hexadecimal representation of the hash
    return hash_object.hexdigest()

def assert_hash(data, expected_hash):
    """
    Assert that the given data, when hashed, matches the expected hash.

    :param data: The string data to hash and compare.
    :param expected_hash: The expected hexadecimal hash value.
    :return: True if the hash matches, False otherwise.
    """
    if not isinstance(data, str):
        raise TypeError("Data must be a string")
    
    # Generate hash of the data
    generated_hash = generate_hash(data)
    
    # Compare the generated hash with the expected hash
    return generated_hash == expected_hash

