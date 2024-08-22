from ..helpers.hash import assert_hash, generate_hash
from ..helpers.encode_decode import encode_object, encode_bin, bin_to_base64
from ..repositories.event_repository import search_event, create_event

def create_event_service(request, data):
    new_event = create_event(request=request,data=data)
    return [{}, "success"]