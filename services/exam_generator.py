from openai import OpenAI
from dotenv import load_dotenv
from core.prompt_builder import build_exam_prompt
from config.settings import MODEL_NAME

load_dotenv()


def generate_exam(level, dyslexia=False):
    """
    Generates a language exam by calling the OpenAI API.

    Builds the prompt for the given level and dyslexia preference,
    sends it to the model, and returns the raw text response.

    Args:
        level (str): CEFR level for the exam (e.g., "A2", "B1", "B2").
        dyslexia (bool): If True, requests dyslexia-friendly formatting. Defaults to False.

    Returns:
        str: The generated exam as plain text.
    """
    client = OpenAI()
    prompt = build_exam_prompt(level, dyslexia)

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are an expert exam generator."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2000
    )

    return response.choices[0].message.content