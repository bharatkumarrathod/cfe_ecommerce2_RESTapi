

def jwt_response_payload_handler(token, user, request, *args, **kwargs):
    data = {
        'token': token,
        'user': user.id,
    }
    return data
