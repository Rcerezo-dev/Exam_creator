def load_prompt(template_name):
    with open(f"core/prompts/{template_name}.txt", "r") as f:
        return f.read()
    
def build_exam_prompt (level, dyslexia):
    template = load_prompt("exam_template")
    prompt = template.replace("{level}", level)
    if dyslexia:
        prompt += "\n\nPlease make the questions dyslexia-friendly."
        prompt += "that means using clear fonts, high contrast, and avoiding complex layouts."
  
    prompt = template.format(
        level=level,
        adaptation=adaptation
    )
    return prompt