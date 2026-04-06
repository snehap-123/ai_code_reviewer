def generate_suggestions(code):
    suggestions = []

    if "range(len(" in code:
        suggestions.append("Use direct iteration instead of range(len())")

    if "== None" in code:
        suggestions.append("Use 'is None' instead of '== None'")

    if "!=" in code and "None" in code:
        suggestions.append("Use 'is not None' instead of '!= None'")

    if "print(" in code:
        suggestions.append("Avoid unnecessary print statements in production")

    if len(code.split("\n")) > 40:
        suggestions.append("Code is too long, consider splitting into functions")

    return suggestions