import json
import re

def extract_json(text):
    """
    Extracts the first JSON block found in a raw text string.

    Uses a regex to locate the content between the first `{` and last `}`
    in the model's response, which may include surrounding explanation text.

    Args:
        text (str): Raw text output from the model.

    Returns:
        str: The extracted JSON string.

    Raises:
        ValueError: If no JSON block is found in the text.
    """
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        return match.group(0)
    raise ValueError("No se encontró un bloque JSON en el texto.")


def parse_json_safely(text):
    """
    Extracts and parses a JSON block from raw model output.

    Combines extraction and parsing into a single step, wrapping both
    in a unified error for easier debugging.

    Args:
        text (str): Raw text output from the model.

    Returns:
        dict: Parsed JSON as a Python dictionary.

    Raises:
        ValueError: If extraction or JSON parsing fails.
    """
    try:
        json_str = extract_json(text)
        return json.loads(json_str)
    except Exception as e:
        raise ValueError(f"Error parsing JSON: {e}")


def validate_writing_response(data):
    """
    Validates that a parsed writing correction response contains all required fields.

    Expected fields: "grammar", "vocabulary", "structure", "feedback".

    Args:
        data (dict): Parsed response from the model.

    Returns:
        dict: The same data, unchanged, if all fields are present.

    Raises:
        ValueError: If any required field is missing.
    """
    required_fields = ["grammar", "vocabulary", "structure", "feedback"]

    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing field: {field}")

    return data