from ..helpers.models import ResPartner

def search_res_partner(request, domain, limit):
    return ResPartner(request.env).search(domain, limit=limit)

def create_res_partner(request, data):
    return ResPartner(request.env).create(data)