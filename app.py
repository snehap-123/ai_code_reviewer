from flask import Flask, render_template, request
from scoring import calculate_score
from suggestion_engine import generate_suggestions
from pylint_engine import run_pylint
from improver import improve_code

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    errors, warnings , suggestions, score = [], [], [], 0
    improved_code = ""

    if request.method == "POST":
        code = request.form["code"].replace("\r", "")
        
        with open("temp.py", "w") as f:
            f.write(code)

        errors, warnings = run_pylint("temp.py")
        suggestions = generate_suggestions(code)
        if suggestions:
            improved_code = improve_code(code)
        else:
            improved_code = ""
        score = calculate_score(errors, warnings, suggestions)
        improved_code = improve_code(code)
        
    return render_template("index.html",
                       errors=errors,
                       warnings=warnings,
                       suggestions=suggestions,
                       score = score,
                       improved_code = improved_code)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
