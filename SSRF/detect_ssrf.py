from flask import Flask, request, jsonify
import requests
from urllib.parse import urlparse

app = Flask(__name__)

ALLOWED_DOMAINS = {
    "example.com",
    "api.github.com",
    "openai.com",
}

def is_allowed_url(url):
    """Check if the URL is in the allowlist"""
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc  # Extract domain (e.g., example.com)
        return domain in ALLOWED_DOMAINS
    except Exception:
        return False

@app.route('/proxy', methods=['GET'])
def proxy_request():
    url = request.args.get("url")  # Get the user-provided URL

    if not url:
        return jsonify({"error": "Missing URL parameter"}), 400
    
    if not is_allowed_url(url):
        print(f"[BLOCKED] {url} is not in the allowlist.")
        return jsonify({"error": "Access to this domain is not allowed!"}), 403

    try:
        response = requests.get(url)
        return jsonify({
            "status": response.status_code,
            "content": response.text
        })
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("SSRF Protection Proxy Running with URL Allowlist...")
    app.run(host="0.0.0.0", port=5000)
