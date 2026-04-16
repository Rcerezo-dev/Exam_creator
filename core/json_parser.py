import json
import re

def extract_json (text):
    """Extrae el primer bloque Json de un texto"""
    match = re.search(r"/{.*\}/", text, re.DOTALL)
    if match:
        return match.group(0)
    raise ValueError("No se encontró un bloque JSON en el texto.")


def parse_json_safely(text):
    try:
        json_str = extract_json(text)
        return json.loads(json_str)
    
    except Exception as e:
        raise ValueError(f"Error parsing JSON: {e}")
    

def validate_writing_response(data):
    required_fields = ["grammar", "vocabulary", "structure", "feedback"]

    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing field: {field}")

    return data