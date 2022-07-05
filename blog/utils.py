import uuid


def get_random_code():
    code = str(uuid.uuid4())
    code_new = code.split('-')
    return (''.join([str(elem) for elem in code_new]))[0:10]

