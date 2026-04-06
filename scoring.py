def calculate_score(errors, warnings, suggestions):
    score = 10

    score -= len(errors) * 2
    score -= len(warnings) * 1
    score -= len(suggestions) * 0.5

    return round(max(score, 0), 2)