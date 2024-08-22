import json
import logging
def extract_fields_from_request(data, required_fields):
    """
    Extracts fields from the given JSON data.
    Raises a validation error if any of the required fields are missing.
    
    :param data: JSON data from request.httprequest.data
    :param required_fields: List of keys that are required in the JSON data
    :return: A dictionary with the extracted fields
    """
    try:
        # Parse the JSON data
        json_data = json.loads(data)
    except json.JSONDecodeError:
        raise Exception("Invalid JSON format")

    # Initialize a dictionary to hold the extracted fields
    extracted_data = {}

    # Iterate through the required fields
    for field in required_fields:
        if field not in json_data:
            raise Exception(f"Missing required field: {field}")
        extracted_data[field] = json_data[field]
    
    return extracted_data

def extract_multipart_fields(request, required_fields):
    """
    Extract fields from a multipart/form-data request.
    Raises a validation error if any of the required fields are missing.
    
    :param request: The HTTP request object.
    :param required_fields: List of keys that are required in the form-data.
    :return: A dictionary with the extracted fields and files.
    """
    extracted_data = {}
    
    for field in required_fields:
        logging.info(f'looww {request.get_http_params()}')
        if field not in request.params and field not in request.httprequest.files:
            raise ValueError(f"Missing required field: {field}")
        
        if field in request.params:
            extracted_data[field] = request.params.get(field)
        
        if field in request.httprequest.files:
            extracted_data[field] = request.httprequest.files.get(field)
    
    return extracted_data

