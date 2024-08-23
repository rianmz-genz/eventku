from ..helpers.encode_decode import encode_bin, bin_to_base64
from ..repositories.event_repository import search_event, create_event
from ..helpers.date import convert_date_local, convert_date_local_back

def create_event_service(request, data):
    exsisting_event = search_event(request=request,domain=[('name', '=', data['name'])],limit=1)
    if exsisting_event:
        raise Exception("Event sudah ada, tolong buat nama sedikit unique")
    data_to_create = {
        **data, 
        'organizer_id': request.env.user['id'],
        'badge_image': encode_bin(image_binary=data['badge_image']),
        'date_begin': convert_date_local(data['date_begin']),
        'date_end': convert_date_local(data['date_end']),
        }
    new_event = create_event(request=request,data=data_to_create)
    return [{'id': new_event.id}, "success"]

def get_event_by_organizer_service(request):
    events = search_event(request=request,domain=[('organizer_id', '=', request.env.user['id'])],limit=None)
    
    return [
        [{
        'id': event.id,
        'name': event.name,
        'organizer_id': event.organizer_id.name,
        "seats_limited": event.seats_limited,
        "seats_max": event.seats_max,
        'date_begin': convert_date_local_back(event.date_begin),
        'date_end': convert_date_local_back(event.date_end), 
        'badge_image': bin_to_base64(image_binary=event.badge_image),
        } for event in events], 
            "success"
            ]