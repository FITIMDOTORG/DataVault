from flask import request, jsonify

def authenticate(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        if token == "valid_token":  # Replace with real authentication
            return func(*args, **kwargs)
        return jsonify({"error": "Unauthorized"}), 401
    return wrapper
