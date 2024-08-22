import json
import base64

def bin_to_base64(image_binary):
    """
    Converts binary data to a base64-encoded ASCII string.
    """
    return image_binary.decode('ascii') if image_binary else ''

def encode_bin(image_binary):
    return base64.b64encode(image_binary.read()) if image_binary else False

def encode_object(obj):
    """
    Encodes a Python dictionary into a base64 string.
    
    :param obj: The dictionary to encode
    :return: Base64 encoded string
    """
    # Convert dictionary to JSON string
    json_str = json.dumps(obj)
    # Encode JSON string to base64
    base64_bytes = base64.b64encode(json_str.encode('utf-8'))
    base64_str = base64_bytes.decode('utf-8')
    return base64_str

def decode_object(base64_str):
    """
    Decodes a base64 string back into a Python dictionary.
    
    :param base64_str: Base64 encoded string
    :return: Original Python dictionary
    """
    # Decode base64 string to JSON string
    json_bytes = base64.b64decode(base64_str.encode('utf-8'))
    json_str = json_bytes.decode('utf-8')
    # Convert JSON string to dictionary
    obj = json.loads(json_str)
    return obj