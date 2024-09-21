import openai

from functions.database import get_recent_messages


# Retrieve Enviornment Variables
openai.organization = ""
openai.api_key = "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"


# Open AI - Whisper
# Convert audio to text
def convert_audio_to_text(audio_file):
  try:
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    message_text = transcript["text"]
    return message_text
  except Exception as e:
    print(f"Error during transcription: {e}")
    return None


# Open AI - Chat GPT
# Convert audio to text
def get_chat_response(message_input):

  messages = get_recent_messages()
  user_message = {"role": "user", "content": message_input }
  messages.append(user_message)

  try:
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
    )
    message_text = response["choices"][0]["message"]["content"]
    return message_text
  except Exception as e:
    print("Model Result Error",e)
    return
