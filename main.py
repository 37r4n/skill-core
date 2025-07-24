import time
from core.handler import handler

print(handler(params={
  "intent": "guess_number",
  "slots": {
    "assistant_number": 9,
    "user_number": 9,
  }
}))
