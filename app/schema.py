from jsonschema import validate
import json

schema_1 = {
  "type": "object",
  "properties": {
    "id": {"type": "string"},
    "beautyTitle": {"type": "string"},
    "title": {"type": "string"},
    "other_titles": {"type": "string"},
    "connect": {"type": "string"},  # что соединяет

    "add_time": {"type": "string"},
    "user": {},  # допустимы поля id, email, phone, fam, name, otc

    "coords": {
      "latitude": {"type": "string"},
      "longitude": {"type": "string"},
      "height": {"type": "string"},
    },
    "type": {"type": "string"},  # константа для всех запросов приложения

    "level": {
      "winter": {"type": "string"},  # текстовое поле "Категория трудности"
      "summer": {"type": "string"},
      "autumn": {"type": "string"},
      "spring": {"type": "string"}
      },

      "images": {
        "type": "array",
        "minItems": 1,
      }
    },
  "required": ["beautyTitle", "images"]
  }


with open("json.txt", "r") as file:
  data = file.read()
  json = json.loads(data)

  validate(json, schema_1)


