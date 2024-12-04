from flask import Flask, request, jsonify
from auth import authenticate
from storage import upload_file, get_file

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
@authenticate
def upload():
    file = request.files["file"]
    token = upload_file(file)
    return jsonify({"token": token})

@app.route("/file/<token>", methods=["GET"])
@authenticate
def fetch_file(token):
    file = get_file(token)
    return file

if __name__ == "__main__":
    app.run(debug=True)
