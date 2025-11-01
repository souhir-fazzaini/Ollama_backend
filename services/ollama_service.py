import json

import requests

OLLAMA_API = "http://localhost:11434/api/chat"

def ask_ollama(model: str, prompt: str):
    payload = {"model": model, "messages": [{"role": "user", "content": prompt}]}
    res = requests.post(OLLAMA_API, json=payload)
    res.raise_for_status()

    # Découper par ligne car Ollama renvoie du streaming JSON
    lines = res.text.splitlines()
    full_response = ""
    print("lines",lines)

    for line in lines:
        try:
            data = json.loads(line)
            full_response += data["message"]["content"]
        except:
            continue

    return full_response
