import os
from uuid import uuid4

STORAGE_DIR = "storage/"

def upload_file(file):
    if not os.path.exists(STORAGE_DIR):
        os.makedirs(STORAGE_DIR)
    token = str(uuid4())
    file.save(os.path.join(STORAGE_DIR, token))
    return token

def get_file(token):
    file_path = os.path.join(STORAGE_DIR, token)
    if os.path.exists(file_path):
        return open(file_path, "rb").read()
    return None
