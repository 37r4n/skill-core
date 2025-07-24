import locale
from datetime import datetime

def handler(params):
  locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
  now = datetime.now()
  date = now.strftime("%A %d de %B de %Y")

  return {
    "output_speech":{
      "type": "plain_text",
      "text": f"Hoy es {date}."
    },
    "end_session": True
  }