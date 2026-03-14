from flask import Flask, jsonify


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_mapping(JSON_AS_ASCII=False)

    @app.get("/api/health")
    def health():
        return jsonify({"status": "ok"})

    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5000, debug=True)
