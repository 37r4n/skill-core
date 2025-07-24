import time
from core.handler import handler

print(handler(params={
  "intent": "calculator",
  "slots": {
    "number_1": 3,
    "number_2": 0,
    "operator": ""
  }
}))
