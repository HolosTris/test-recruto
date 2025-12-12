import os
from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    name = request.args.get("name", "Recruto")
    message = request.args.get("message", "Давай дружить!")

    safe_name = escape(name)
    safe_message = escape(message)
    return f"Hello {safe_name}! {safe_message}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
