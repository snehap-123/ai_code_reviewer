def improve_code(code):
    improved = code

    changed = False  # 

    if "== None" in improved:
        improved = improved.replace("== None", "is None")
        changed = True

    if "!= None" in improved:
        improved = improved.replace("!= None", "is not None")
        changed = True

    if "range(len(" in improved:
        improved = improved.replace("for i in range(len(", "for i in ")
        changed = True

    if changed:
        return improved
    else:
        return ""   