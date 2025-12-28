from urllib.parse import urlparse

def extract_features(url):
    features = []
    parsed = urlparse(url)
    
    # Existing features
    features.append(len(url))                         # URL Length
    features.append(1 if "@" in url else 0)           # '@' Symbol
    features.append(1 if "//" in parsed.path else 0)  # Redirect
    features.append(1 if "-" in parsed.netloc else 0) # '-' Symbol
    features.append(1 if parsed.scheme == "https" else 0) # SSL

    # New features
    features.append(len(parsed.netloc)) # Domain Length
    features.append(parsed.netloc.count('.')) # Number of subdomains
    features.append(len(parsed.path)) # Path Length
    sensitive_words = ["login", "secure", "account", "update", "banking", "signin"]
    features.append(1 if any(word in url.lower() for word in sensitive_words) else 0) # Presence of sensitive words

    return features
