from ..helpers.models import Event

def search_res_event(request, domain, limit):
    return Event(request.env).search(domain, limit=limit)

def create_res_event(request, data):
    return Event(request.env).create(data)