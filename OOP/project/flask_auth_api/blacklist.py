from flask_jwt_extended import get_jwt
import blacklist

BLACKLIST = set()

def add_token(token):
    BLACKLIST.add(token)

def is_blacklisted(token):
    return token in BLACKLIST
