import random

def handler(params):
  slots = params.get("slots")
  assistant_number = slots.get('assistant_number')
  user_number = slots.get('user_number')

  if not assistant_number:
    assistant_number = random.randint(1,10)

    return {
      "output_speech":{
        "type": "plain_text",
        "text": f"Estoy pensando en un numero del 1 al 10. Intenta adivinarlo."
      },
      "end_session": False,
      "slots":{
        "assistant_number": assistant_number
      }
    }
  
  assistant_number = int(assistant_number)
  user_number = int(user_number)
  
  if(user_number ==assistant_number):
    return {
      "output_speech":{
        "type": "plain_text",
        "text": f"¡Correcto! Era el {assistant_number}. Buen trabajo."
      },
      "end_session": True,
    }
  
  if(user_number < assistant_number):
    return {
      "output_speech":{
        "type": "plain_text",
        "text": "Mi número es más grande."
      },
      "end_session": False,
      "slots":{
        "assistant_number": assistant_number
      }
    }
  
  if(user_number > assistant_number):
    return {
      "output_speech":{
        "type": "plain_text",
        "text": "Mi número es más pequeño."
      },
      "end_session": False,
      "slots":{
        "assistant_number": assistant_number
      }
    }