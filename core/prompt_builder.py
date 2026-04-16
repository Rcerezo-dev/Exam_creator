def load_prompt(template_name):
    """
    Loads a prompt template from the prompts directory.

    Args:
        template_name (str): Name of the template file without extension
                             (e.g., "exam_template" → prompts/exam_template.txt).

    Returns:
        str: Raw content of the template file.
    """
    with open(f"core/prompts/{template_name}.txt", "r") as f:
        return f.read()


def build_exam_prompt(level, dyslexia):
    """
    Builds the exam generation prompt by injecting parameters into the template.

    Derives the adaptation string from the dyslexia flag and uses
    template.format() to fill in both {level} and {adaptation} placeholders.

    Args:
        level (str): CEFR level for the exam (e.g., "A2", "B1", "B2").
        dyslexia (bool): If True, requests dyslexia-friendly formatting.

    Returns:
        str: The complete prompt ready to send to the model.
    """
    template = load_prompt("exam_template")

    if dyslexia:
        adaptation = "Make the exam dyslexia-friendly: use clear fonts, high contrast, and avoid complex layouts."
    else:
        adaptation = "None"

    prompt = template.format(
        level=level,
        adaptation=adaptation
    )
    return prompt


def build_writing_prompt(text, level, dyslexia):
    """
    Builds the writing correction prompt by injecting parameters into the template.

    Derives the adaptation string from the dyslexia flag and uses
    template.format() to fill in {level}, {text}, and {adaptation} placeholders.

    Args:
        text (str): The student's writing to evaluate.
        level (str): CEFR level to calibrate scoring expectations.
        dyslexia (bool): If True, requests dyslexia-aware evaluation.

    Returns:
        str: The complete prompt ready to send to the model.
    """
    template = load_prompt("writing")

    if dyslexia:
        adaptation = "Be lenient with layout and formatting issues, as the student may have dyslexia."
    else:
        adaptation = "None"

    prompt = template.format(
        text=text,
        level=level,
        adaptation=adaptation
    )
    return prompt