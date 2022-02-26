
schema = {
  "type": "object",
  "properties": {
    "id": {"type": "string"},
    "beautyTitle": {"type": "string"},
    "title": {"type": "string"},
    "other_titles": {"type": "string"},
    "connect": {"type": "string"},  # что соединяет

    "add_time": {"type": "string"},
    "user": {"type": "object"},  # допустимы поля id, email, phone, fam, name, otc

    "coords": {
      "latitude": {"type": "string"},
      "longitude": {"type": "string"},
      "height": {"type": "string"},
      "required": ["latitude", "longitude", "height"]
    },

    "type": {"type": "string"},  # константа для всех запросов приложения

    "level": {
      "winter": {"type": "string"},  # текстовое поле "Категория трудности"
      "summer": {"type": "string"},
      "autumn": {"type": "string"},
      "spring": {"type": "string"},
      "required": ["winter", "summer", "autumn", "spring"]
      },

    "images": {
        "type": "array",
        "minItems": 1,
      },

    },
  "required": ["id", "beautyTitle", "title", "other_titles", "connect", "user", "coords", "type", "level", "images"],
  "additionalProperties": False
}

