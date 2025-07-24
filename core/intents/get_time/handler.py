from datetime import datetime

def handler(params):
  now = datetime.now()
  time = now.strftime("%H:%M")

  return {
    "output_speech":{
      "type": "plain_text",
      "text": f"Son las {time}."
    },
    "end_session": True
  }