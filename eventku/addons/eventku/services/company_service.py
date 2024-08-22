from ..helpers.hash import assert_hash, generate_hash
from ..helpers.encode_decode import encode_object, encode_bin, bin_to_base64
from ..repositories.res_partner_repository import search_res_partner, create_res_partner

def login_service(request, data):
    company = search_res_partner(request=request,domain=[('email', '=', data['email'])],limit=1)
    
    if not company:
        raise Exception("Invalid credentials")
    
    if not assert_hash(data['password'], company.street):
        raise Exception("Invalid credentials")

    return [{
        'token': encode_object({
            'id': company.id,
            'name': company.name
        })
    }, "Succes to login"]

def register_service(request, data):
    existing_company =  search_res_partner(request=request,domain=[
        '|',  # OR condition
        ('email', '=', data['email']),
        ('name', '=', data['name'])  # Adjusted to include name check
    ], limit=1)
    
    if existing_company:
        raise Exception("Email or name already registered")

    
    # Hash password
    hashed_password = generate_hash(data['password'])
    
    # Membuat perusahaan baru dengan email dan password hash
    new_company = create_res_partner(request=request,data={
        'email': data['email'],
        'street': hashed_password,
        'name': data['name'],
        'image_1920': encode_bin(data['logo']),
    })
    
    return [{
        'id': new_company.id,
        'email': new_company.email,
        'name': new_company.name,
        'logo': bin_to_base64(new_company.image_1024)
    },"Registration successful"]