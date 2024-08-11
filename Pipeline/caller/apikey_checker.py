def is_openai_apikey(apikey: str):
    return apikey.startswith("sk-")

def is_google_apikey(apikey: str):
    return apikey.startswith("AI")

def is_anthropic_apikey(apikey: str):
    return apikey.startswith("sk-")