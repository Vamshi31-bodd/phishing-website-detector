from flask import Flask, render_template, request
import sys
from urllib.parse import urlparse

sys.path.append("src")

from predict import predict_url


app = Flask(__name__)


def valid_url(url):
    try:
        parsed = urlparse(url)

        if parsed.scheme not in ["http", "https"]:
            return False

        if not parsed.netloc:
            return False

        return True

    except Exception:
        return False


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    confidence = None
    url = ""
    error = None

    if request.method == "POST":

        url = request.form.get("url", "").strip()

        if not url:
            error = "Please enter a website URL."

        elif not valid_url(url):
            error = "Please enter a valid URL starting with http:// or https://"

        else:
            try:
                result, confidence = predict_url(url)

            except Exception:
                error = "Unable to analyze this URL. Please try again."

    return render_template(
        "index.html",
        result=result,
        confidence=confidence,
        url=url,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)