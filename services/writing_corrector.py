from openai import OpenAI
from dotenv import load_dotenv
from core.prompt_builder import build_writing_prompt
from core.json_parser import parse_json_safely, validate_writing_response
from config.settings import MODEL_NAME

load_dotenv()

client = OpenAI()


def correct_writing(text, level, dyslexia):
    """
    Evaluates a student's writing sample and returns structured feedback.

    Builds a correction prompt, calls the model, and parses the response
    into a validated dictionary with scores and feedback.

    Args:
        text (str): The student's writing to evaluate.
        level (str): CEFR level to calibrate expectations (e.g., "A2", "B1").
        dyslexia (bool): If True, adjusts the prompt for dyslexia-friendly evaluation.

    Returns:
        dict: Validated response with keys:
              - "grammar" (int): Score 0–10
              - "vocabulary" (int): Score 0–10
              - "structure" (int): Score 0–10
              - "feedback" (str): Short, clear feedback for the student
    """
    # 1. Crear prompt
    prompt = build_writing_prompt(text, level, dyslexia)

    # 2. Llamar al modelo
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    # 3. Obtener texto
    raw_output = response.choices[0].message.content

    # 4. Parsear JSON
    parsed = parse_json_safely(raw_output)

    # 5. Validar
    validated = validate_writing_response(parsed)

    return validated