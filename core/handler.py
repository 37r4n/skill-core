from .intents import get_date, get_time, tell_joke, calculator, guess_number

def handler(params):
  intent = params.get('intent')
  slots = params.get('slots')
  device = params.get('device')

  if intent == "calculator":
    return calculator.handler(params)

  if intent == 'get_date':
    return get_date.handler(params)
  
  if intent == 'get_time':
    return get_time.handler(params)
  
  if intent == 'tell_joke':
    return tell_joke.handler(params)

  if intent == 'guess_number':
    return guess_number.handler(params)