from urllib.parse import urlparse
import re
import math


def extract_features(url):

    # Add scheme if missing
    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    parsed = urlparse(url)

    domain = parsed.netloc.lower()
    path = parsed.path
    query = parsed.query

    # Remove port
    domain = domain.split(":")[0]

    features = {}

    # Basic URL features
    features["url_length"] = len(url)
    features["domain_length"] = len(domain)
    features["path_length"] = len(path)

    # IP address
    features["has_ip"] = int(
        bool(re.fullmatch(r"\d{1,3}(\.\d{1,3}){3}", domain))
    )

    # HTTPS
    features["is_https"] = int(parsed.scheme == "https")

    # Subdomains
    parts = domain.split(".")
    features["subdomain_count"] = max(0, len(parts) - 2)

    # URL characters
    features["digit_count"] = sum(c.isdigit() for c in url)
    features["letter_count"] = sum(c.isalpha() for c in url)

    features["special_char_count"] = sum(
        not c.isalnum() for c in url
    )

    # Suspicious characters
    features["has_at"] = int("@" in url)
    features["has_double_slash"] = int("//" in path)
    features["has_hyphen_domain"] = int("-" in domain)
    features["has_question_mark"] = int("?" in url)
    features["has_equal"] = int("=" in url)
    features["has_ampersand"] = int("&" in url)

    # URL structure
    features["query_length"] = len(query)

    # Percent encoding
    features["percent_count"] = url.count("%")

    # Digit ratio
    features["digit_ratio"] = (
        features["digit_count"] / len(url)
        if len(url) > 0 else 0
    )

    # Letter ratio
    features["letter_ratio"] = (
        features["letter_count"] / len(url)
        if len(url) > 0 else 0
    )

    # Suspicious words
    suspicious_words = [
        "login",
        "signin",
        "verify",
        "verification",
        "account",
        "update",
        "secure",
        "security",
        "password",
        "bank",
        "paypal",
        "payment",
        "confirm",
        "credential",
        "wallet",
        "bonus",
        "free",
        "support"
    ]

    url_lower = url.lower()

    features["suspicious_word_count"] = sum(
        word in url_lower
        for word in suspicious_words
    )

    # Entropy
    frequency = {}

    for char in url:
        frequency[char] = frequency.get(char, 0) + 1

    entropy = 0

    for count in frequency.values():
        probability = count / len(url)
        entropy -= probability * math.log2(probability)

    features["url_entropy"] = entropy

    return features