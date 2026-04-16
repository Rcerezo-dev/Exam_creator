from openai import OpenAI
from core.prompt_builder import build_exam_prompt

def generate_exam(level, dyslexia=False):
    client = OpenAI()
    prompt = build_exam_prompt(level, dyslexia)
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert exam generator."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2000
    )
    
    return response.choices[0].message.content