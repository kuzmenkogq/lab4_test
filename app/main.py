from flask import Flask, request, jsonify
from app.password_generator import generate_password

app = Flask(__name__)


@app.route("/generate-password", methods=["POST"])
def generate():
    data = request.get_json()
    try:
        length = int(data.get("length", 12))
        use_digits = bool(data.get("use_digits", True))
        use_symbols = bool(data.get("use_symbols", True))
        use_uppercase = bool(data.get("use_uppercase", True))

        password = generate_password(
            length,
            use_digits,
            use_symbols,
            use_uppercase
        )
        return jsonify({"password": password})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
