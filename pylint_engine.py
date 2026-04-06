import subprocess
import json
import sys

def run_pylint(file_path):
    result = subprocess.run(
        [sys.executable, "-m", "pylint", file_path, "--output-format=json"],
        capture_output=True,
        text=True
    )

    try:
        data = json.loads(result.stdout)
    except:
        data = []

    errors = []
    warnings = []

    for item in data:
        message = f"{item['message']} (Line {item['line']})"

        if item['type'] == 'error':
            errors.append(message)
        else:
            warnings.append(message)

    return errors, warnings