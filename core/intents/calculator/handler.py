from .constants import OPERATORS

def handler(params):
    slots = params.get("slots", {})
    number_1 = float(slots.get("number_1", 0))
    number_2 = float(slots.get("number_2", 0))
    symbol = slots.get("operator")

    if symbol not in OPERATORS:
      return {
        "output_speech":{
        "type": "plain_text",
        "text": "¿Qué operación deseas realizar?"
        },
        "end_session": False,
        "slots":{
           "number_1": number_1,
           "number_2": number_2
        }
      }

    if symbol == "/" and number_2 == 0:
      return {
        "output_speech":{
        "type": "plain_text",
        "text": 'No puedo dividir por cero.'
        },
        "end_session": True
      }

    result = OPERATORS[symbol](number_1, number_2)
    if float(result).is_integer():
        result = int(result)
    else:
        result = round(result, 2)

    return {
      "output_speech":{
      "type": "plain_text",
      "text": str(result)
      },
      "end_session": True
    }