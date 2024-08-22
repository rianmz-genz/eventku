from functools import wraps
from odoo.http import Response, request
from ..helpers.encode_decode import decode_object
import json
import logging
logger = logging.getLogger(__name__)
class AuthUtility:
    @staticmethod
    def authenticate():
        """Perform custom authentication logic."""
        token_base64 = request.httprequest.headers.get('Authorization')
        if not token_base64:
            return None
        
        user_id = False
        try:
            user_id = decode_object(base64_str=token_base64)
        except Exception as e:
            raise Exception("Invalid token_base64")
        
        logger.info(f"Token_base64: {token_base64}, User: {user_id}")
        return user_id if user_id else None


def custom_auth_required(method):
    @wraps(method)
    def wrapper(*args, **kwargs):
        try:
            user = AuthUtility.authenticate()
            if user:
                request.env.user = user
                return method(*args, **kwargs)
            else:
                return Response(json.dumps({'message': 'Unauthorized'}),content_type="application/json", status=401)
        except Exception as e:
            return Response(json.dumps({'message': f'{e}'}),content_type="application/json", status=401)
    return wrapper
