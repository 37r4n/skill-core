import random
from .constants import JOKES

def handler(params):
  joke = random.choice(JOKES)

  return {
    "output_speech":{
      "type": "plain_text",
      "text": joke
    },
    "end_session": True
  }
