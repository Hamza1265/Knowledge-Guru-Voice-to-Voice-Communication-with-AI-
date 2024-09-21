import requests

ELEVEN_LABS_API_KEY = "35aff3f003f009a88acde7c60af2b6bd"

# Eleven Labs
# Convert text to speech
def convert_text_to_speech(message):
    # Verify API key
    if not ELEVEN_LABS_API_KEY:
        raise ValueError("ELEVEN_LABS_API_KEY is missing")

    # Ensure message is not empty
    if not message:
        raise ValueError("Message is empty")

    # Check voice ID
    voice_id = "2gPFXx8pN3Avh27Dw5Ma"  # Default voice ID
    # Verify if voice ID is correct
    if not voice_id:
        raise ValueError("Invalid voice ID")

    # Request body and headers
    body = {
        "text": message,
        "voice_settings": {
            "stability": 0.5,  # Ensure these values are within valid ranges
            "similarity_boost": 0.5,
        },
    }

    headers = {
        "xi-api-key": "35aff3f003f009a88acde7c60af2b6bd",
        "Content-Type": "application/json",
        "accept": "audio/mpeg",
    }

    endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    try:
        response = requests.post(endpoint, json=body, headers=headers)
        response.raise_for_status()  # Raise HTTP error if not 200
        return response.content
    except requests.exceptions.RequestException as e:
        print("Voice to Audio Error:", e)
        return None
