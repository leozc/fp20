import json
import hashlib

# accept a json object and return a signed string
def sign(jsonobj):
    """
    return string of a RAW ordered json object
    """
    # convert json to string
    j = json.dumps(jsonobj, sort_keys=True)

    return hashlib.md5(j.encode('utf-8')).hexdigest()

def verifysign(jsonobj, signature):
    """
    return True if the token is the same as the signed string of the json object
    """
    return signature == sign(jsonobj)